import collections
import xmltodict
from pathlib import Path

from data_fetching.data_scraping import DataFetcher, DataParser, DataCleaner

Response = collections.namedtuple("Response", "status_code text")

with open(Path(__file__).parent.absolute().joinpath("fixture.rss"), "r") as f:
    DATA = xmltodict.parse(f.read())


class RequestMock:
    def get(self, link):
        status_code, text = link.split("_")
        return Response(status_code=int(status_code), text=text)


class ParserMock:
    def parse(self, data):
        return data


def test_data_fetcher_200():
    assert DataFetcher("200_link", RequestMock()).make_request() == "link"


def test_data_fetcher_404():
    assert DataFetcher("404_link", RequestMock()).make_request() == ""


def test_data_parser():
    raw_data = "test"
    assert DataParser(raw_data, ParserMock()).parse_data() == "test"


def test_data_cleaner():
    cleaner = DataCleaner(DATA)
    assert cleaner.exchange_rate == "1.0898"
    assert cleaner.base_currency == "EUR"
    assert cleaner.target_currency == "USD"
    assert cleaner.date == "2019-10-01"

