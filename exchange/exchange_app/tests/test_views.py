from django.test import TestCase
from exchange_app.models import ExchangeRate, Currency
from collections import OrderedDict


class ExchangeRateViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        currency_eur = Currency.objects.create(
            base_currency="EUR", target_currency="PLN"
        )
        currency_gbp = Currency.objects.create(
            base_currency="EUR", target_currency="GBP"
        )

        ExchangeRate.objects.create(
            exchange_rate=1.02, currency=currency_eur, date="2019-01-01"
        )
        ExchangeRate.objects.create(
            exchange_rate=1.03, currency=currency_eur, date="2019-01-02"
        )
        ExchangeRate.objects.create(
            exchange_rate=1.04, currency=currency_gbp, date="2019-01-02"
        )

    def test_get_exchange_rate_for_currency(self):
        response = self.client.get("/api/exchange_rates/all/PLN")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            [
                OrderedDict(
                    [
                        ("exchange_rate", "1.02000000"),
                        ("date", "2019-01-01"),
                        (
                            "currency",
                            OrderedDict(
                                [("base_currency", "EUR"), ("target_currency", "PLN")]
                            ),
                        ),
                    ]
                ),
                OrderedDict(
                    [
                        ("exchange_rate", "1.03000000"),
                        ("date", "2019-01-02"),
                        (
                            "currency",
                            OrderedDict(
                                [("base_currency", "EUR"), ("target_currency", "PLN")]
                            ),
                        ),
                    ]
                ),
            ],
        )

    def test_get_last_exchange_rate_for_currency(self):
        response = self.client.get("/api/exchange_rates/PLN")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "exchange_rate": "1.03000000",
                "date": "2019-01-02",
                "currency": OrderedDict(
                    [("base_currency", "EUR"), ("target_currency", "PLN")]
                ),
            },
        )

    def test_get_exchange_rate_for_date(self):
        response = self.client.get("/api/exchange_rates/2019-01-02")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            [
                OrderedDict(
                    [
                        ("exchange_rate", "1.03000000"),
                        ("date", "2019-01-02"),
                        (
                            "currency",
                            OrderedDict(
                                [("base_currency", "EUR"), ("target_currency", "PLN")]
                            ),
                        ),
                    ]
                ),
                OrderedDict(
                    [
                        ("exchange_rate", "1.04000000"),
                        ("date", "2019-01-02"),
                        (
                            "currency",
                            OrderedDict(
                                [("base_currency", "EUR"), ("target_currency", "GBP")]
                            ),
                        ),
                    ]
                ),
            ],
        )

    def test_get_exchange_rate_for_bad_date(self):
        response = self.client.get("/api/exchange_rates/2019-13-30")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, None)

    def test_get_exchange_rate_for_not_existing_date(self):
        response = self.client.get("/api/exchange_rates/2019-10-01")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_get_last_exchange_rate_for_fake_currency(self):
        response = self.client.get("/api/exchange_rates/ABC")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, None)

    def test_get_exchange_rates_for_fake_currency(self):
        response = self.client.get("/api/exchange_rates/all/ABC")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])
