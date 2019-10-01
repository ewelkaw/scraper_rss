from rest_framework import serializers
from .models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    """
    ExchangeRate Serializer
    Serializer validates the model querysets.
    """

    class Meta:
        model = ExchangeRate
        fields = ("exchange_rate", "base_currency", "target_currency", "date")
