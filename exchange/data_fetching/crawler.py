import sys
from pathlib import Path
from data_fetching.data_scraping import Dispatcher


def run_scrapping():
    print("Scraping")
    sys.stdout.flush()
    path = Path(__file__).absolute().parent.joinpath("links.txt")
    Dispatcher(path).run()
    print("Task finished")
    sys.stdout.flush()
