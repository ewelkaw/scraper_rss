import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exchange.settings")
django.setup()


from datetime import date
from pathlib import Path

from exchange_app.models import ExchangeRate, Currency
from celery.decorators import task
import requests
import xmltodict
from dateutil.parser import parse

from data_fetching.celery import celery_app


class Dispatcher:
    def __init__(self, links_list_path: Path):
        self.links_list_path = links_list_path

    @property
    def links_list(self):
        with open(self.links_list_path, "r") as f:
            data = map(lambda x: x.strip(), f.readlines())
        return data

    @staticmethod
    def prepare_raw_data(link):
        return DataFetcher(link).make_request()

    def run(self):
        for link in self.links_list:
            self.single_pass.delay(link)

    @celery_app.task(name="scrap_data")
    def single_pass(link):
        raw_data = Dispatcher.prepare_raw_data(link)
        if raw_data == "":
            return

        parsed_data = DataParser(raw_data).parse_data()
        cleaned_data = DataCleaner(parsed_data)

        currency, _ = Currency.objects.get_or_create(
            base_currency=cleaned_data.base_currency,
            target_currency=cleaned_data.target_currency,
        )
        ExchangeRate.objects.get_or_create(
            currency=currency,
            date=date(*map(lambda x: int(x), cleaned_data.date.split("-"))),
            defaults={"exchange_rate": cleaned_data.exchange_rate},
        )


class DataFetcher:
    def __init__(self, link, req_module=requests):
        self.link = link
        self.req_module = req_module

    def make_request(self):
        data = self.req_module.get(self.link)
        if data.status_code == 200:
            return data.text
        else:
            return ""


class DataParser:
    def __init__(self, raw_data, data_parser=xmltodict):
        self.raw_data = raw_data
        self.data_parser = data_parser

    def parse_data(self):
        return self.data_parser.parse(self.raw_data)


class DataCleaner:
    def __init__(self, data: dict):
        self.data = data

    @property
    def exchange_rate(self):
        return self.data["rdf:RDF"]["item"][0]["cb:statistics"]["cb:exchangeRate"][
            "cb:value"
        ]["#text"]

    @property
    def base_currency(self):
        return self.data["rdf:RDF"]["item"][0]["cb:statistics"]["cb:exchangeRate"][
            "cb:baseCurrency"
        ]["#text"]

    @property
    def target_currency(self):
        return self.data["rdf:RDF"]["item"][0]["cb:statistics"]["cb:exchangeRate"][
            "cb:targetCurrency"
        ]

    @property
    def date(self):
        return parse(self.data["rdf:RDF"]["item"][0]["dc:date"]).date().isoformat()


if __name__ == "__main__":
    # loading defined path, can be changed in the future
    path = Path(__file__).absolute().parent.joinpath("links.txt")
    Dispatcher(path).run()
