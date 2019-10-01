# Makefile

build:
	docker build . -t scraper

run:
	docker-compose up