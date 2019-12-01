from celery import Celery


class Config:
    enable_utc = True
    timezone = "Europe/Warsaw"
    broker_url = "redis://redis:6379/0"


celery_app = Celery()
celery_app.config_from_object(Config)
