from django.test import TestCase
from exchange_app.serializers import ExchangeRateSerializer
from exchange_app.models import ExchangeRate, Currency
from collections import OrderedDict


class ExchangeRateSerializerTest(TestCase):
    def test_serializer(self):
        currency = Currency(base_currency="EUR", target_currency="PLN")

        rate = ExchangeRate(exchange_rate=1.02, currency=currency, date="2019-01-01")
        serializer = ExchangeRateSerializer(rate, many=False)
        self.assertEqual(
            serializer.data,
            {
                "exchange_rate": "1.02000000",
                "date": "2019-01-01",
                "currency": OrderedDict(
                    [("base_currency", "EUR"), ("target_currency", "PLN")]
                ),
            },
        )

    def test_serializer_many(self):
        currency = Currency(base_currency="EUR", target_currency="PLN")

        rates = [
            ExchangeRate(exchange_rate=1.02, currency=currency, date="2019-01-01"),
            ExchangeRate(exchange_rate=1.02, currency=currency, date="2019-01-02"),
        ]
        serializer = ExchangeRateSerializer(rates, many=True)
        self.assertEqual(
            serializer.data,
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
                        ("exchange_rate", "1.02000000"),
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
