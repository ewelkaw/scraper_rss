from django.shortcuts import render
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer, CurrencySerializer


@api_view(["GET"])
def get_exchange_rate_for_currency(request, currency_shortcut):
    rate = ExchangeRate.objects.filter(
        currency__target_currency=currency_shortcut
    ).order_by("date")
    serializer = ExchangeRateSerializer(rate, many=True)

    # get all records for a single currency shortcut
    return Response(serializer.data)


@api_view(["GET"])
def get_last_exchange_rate_for_currency(request, currency_shortcut):
    rate = (
        ExchangeRate.objects.filter(currency__target_currency=currency_shortcut)
        .order_by("-date")
        .first()
    )
    if not rate:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ExchangeRateSerializer(rate, many=False)

    # get single record with latest data for given currency
    return Response(serializer.data)


@api_view(["GET"])
def get_exchange_rate_for_date(request, given_date):
    try:
        rates = ExchangeRate.objects.filter(
            date=date(*map(lambda x: int(x), given_date.split("-")))
        )
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = ExchangeRateSerializer(rates, many=True)

    # get all currencies details for a single date
    return Response(serializer.data)
