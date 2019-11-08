from rest_framework import serializers
from .models import ExchangeRate, Currency


class CurrencySerializer(serializers.ModelSerializer):
    """
    Currency Serializer
    Serializer validates the model querysets.
    """

    class Meta:
        model = Currency
        fields = ("base_currency", "target_currency")


class ExchangeRateSerializer(serializers.ModelSerializer):
    """
    ExchangeRate Serializer
    Serializer validates the model querysets.
    """

    currency = CurrencySerializer(many=False, read_only=True)

    class Meta:
        model = ExchangeRate
        fields = ("exchange_rate", "date", "currency")

