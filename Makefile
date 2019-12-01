# Makefile

build:
	docker build . -t scraper

run:
	docker-compose up

migrate:
	docker run -it -v "$(PWD)/exchange/db:/app/exchange/db" --rm scraper python3 manage.py migrate

makemigrations:
	docker run -it -v "$(PWD)/exchange/db:/app/exchange/db" --rm scraper python3 manage.py makemigrations

test-django:
	docker run -it --rm scraper python3 manage.py test

test-python:
	docker run -it --rm scraper pytest tests/