from django.test import TestCase

from exchange_app.serializers import ExchangeRateSerializer
from exchange_app.models import ExchangeRate


class ExchangeRateSerializerTest(TestCase):
    def test_serializer(self):
        rate = ExchangeRate(
            exchange_rate=1.02,
            base_currency="EUR",
            target_currency="PLN",
            date="2019-01-01",
        )
        serializer = ExchangeRateSerializer(rate, many=False)
        self.assertEqual(
            serializer.data,
            {
                "exchange_rate": "1.02000000",
                "base_currency": "EUR",
                "target_currency": "PLN",
                "date": "2019-01-01",
            },
        )

    def test_serializer_many(self):
        rates = [
            ExchangeRate(
                exchange_rate=1.02,
                base_currency="EUR",
                target_currency="PLN",
                date="2019-01-01",
            ),
            ExchangeRate(
                exchange_rate=1.02,
                base_currency="EUR",
                target_currency="PLN",
                date="2019-01-02",
            ),
        ]
        serializer = ExchangeRateSerializer(rates, many=True)
        self.assertEqual(
            serializer.data,
            [
                {
                    "exchange_rate": "1.02000000",
                    "base_currency": "EUR",
                    "target_currency": "PLN",
                    "date": "2019-01-01",
                },
                {
                    "exchange_rate": "1.02000000",
                    "base_currency": "EUR",
                    "target_currency": "PLN",
                    "date": "2019-01-02",
                },
            ],
        )
