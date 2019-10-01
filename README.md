# scraper_rss
RSS scraper for reading exchange rates from the European Central Bank web page.

## API USAGE:
1. There is a possibility to use currency shortcut to get all data for given currency like below:
http://127.0.0.1:8000/api/exchange_rates/all/PLN

RESPONSE:
```
[
    {
        "exchange_rate": "4.37740000",
        "base_currency": "EUR",
        "target_currency": "PLN",
        "date": "2019-10-01"
    }
]
```

2. There is another possibility to use currency shortcut to get only latest data for given currency like below:
http://127.0.0.1:8000/api/exchange_rates/PLN

RESPONSE:
```
{
    "exchange_rate": "4.37740000",
    "base_currency": "EUR",
    "target_currency": "PLN",
    "date": "2019-10-01"
}
```

3. There is also a possibility to use date to get proper data like below:
http://127.0.0.1:8000/api/exchange_rates/2019-10-01

RESPONSE:
```
[
    {
        "exchange_rate": "1.08980000",
        "base_currency": "EUR",
        "target_currency": "USD",
        "date": "2019-10-01"
    },
    ...
    {
        "exchange_rate": "16.67000000",
        "base_currency": "EUR",
        "target_currency": "ZAR",
        "date": "2019-10-01"
    }
]
```

## To use django-admin: http://127.0.0.1:8000/admin/ 

Remember to add super user before using that:

```
python manage.py createsuperuser
```

## Tests

### Django tests

```
cd exchange
python manage.py test
```

### Fetcher test

```
cd exchange
pytest tests/
```