from celery import Celery
from .crawler import run_scrapping

app = Celery()


class Config:
    enable_utc = True
    timezone = "Europe/Warsaw"
    broker_url = "redis://redis:6379/0"


app.config_from_object(Config)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0 * 10, crawler_task.s(), name="add every 10")


@app.task
def crawler_task():
    run_scrapping()
