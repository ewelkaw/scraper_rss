from data_fetching.celery import celery_app
from data_fetching.crawler import run_scrapping


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, crawler_task.s(), name="add every 10")


@celery_app.task
def crawler_task():
    run_scrapping()
