import sys
import time
from pathlib import Path
from data_fetching.data_scraping import Dispatcher

while True:
    print("Scraping")
    sys.stdout.flush()
    path = Path(__file__).absolute().parent.joinpath("links.txt")
    Dispatcher(path).run()
    print("Task finished")
    sys.stdout.flush()
    time.sleep(60 * 10)
