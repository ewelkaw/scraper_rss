FROM python:3.6.9-alpine3.10

ENV PYTHONPATH .
RUN apk add --no-cache build-base libffi-dev openssl libressl-dev musl-dev
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . /app
WORKDIR /app/exchange
CMD sh

# docker build . -t scraper