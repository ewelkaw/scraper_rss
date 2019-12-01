# scraper_rss
RSS scraper for reading exchange rates from the European Central Bank web page.

## RUNNING APP:

1. make build
2. make run
3. make migrate
4. make makemigrations

## API USAGE:
1. There is a possibility to use currency shortcut to get all data for given currency like below:
http://127.0.0.1:8000/api/exchange_rates/all/PLN

RESPONSE:
```
[
    {
        "exchange_rate": "4.36980000",
        "date": "2019-10-02",
        "currency": {
            "base_currency": "EUR",
            "target_currency": "PLN"
        }
    }
]
```

2. There is another possibility to use currency shortcut to get only latest data for given currency like below:
http://127.0.0.1:8000/api/exchange_rates/PLN

RESPONSE:
```
{
    "exchange_rate": "4.36980000",
    "date": "2019-10-02",
    "currency": {
        "base_currency": "EUR",
        "target_currency": "PLN"
    }
}
```

3. There is also a possibility to use date to get proper data like below:
http://127.0.0.1:8000/api/exchange_rates/2019-10-02

RESPONSE:
```
[
    {
        "exchange_rate": "1.09250000",
        "date": "2019-10-02",
        "currency": {
            "base_currency": "EUR",
            "target_currency": "USD"
        }
    },
    ...
    {
        "exchange_rate": "16.66270000",
        "date": "2019-10-02",
        "currency": {
            "base_currency": "EUR",
            "target_currency": "ZAR"
        }
    }
]
```

## To use django-admin: http://127.0.0.1:8000/admin/ 

Remember to add super user before using that:

```
python manage.py createsuperuser
```

## TESTS

### Django tests

```
make test-django
```

### Fetcher test

```
make test-python
```