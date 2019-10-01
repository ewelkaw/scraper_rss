from pathlib import Path
import xmltodict
import requests
from datetime import datetime
from dateutil.parser import parse


class Dispatcher:
    def __init__(self, links_list_path):
        self.links_list_path = links_list_path

    @property
    def links_list(self):
        with open(self.links_list_path, "r") as f:
            data = map(lambda x: x.strip(), f.readlines())
        return data

    def run(self):
        raw_data = map(lambda link: DataFetcher(link).make_request(), self.links_list)
        filtered_data = filter(lambda x: x != "", raw_data)
        parsed_data = map(lambda rss: DataParser(rss).parse_data(), filtered_data)
        cleaned_data = map(lambda xml: DataCleaner(xml), parsed_data)
        for data in cleaned_data:
            print(
                "data:",
                data.exchange_rate,
                data.base_currency,
                data.target_currency,
                data.date,
            )
            # ExchangeRate(
            #     data.exchange_rate, data.base_currency, data.target_currency, data.date
            # )


class DataFetcher:
    def __init__(self, link):
        self.link = link

    def make_request(self):
        data = requests.get(self.link)
        if data.status_code == 200:
            return data.text
        else:
            return ""


class DataParser:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def parse_data(self):
        return xmltodict.parse(self.raw_data)


class DataCleaner:
    def __init__(self, data):
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

