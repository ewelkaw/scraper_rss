from django.conf.urls import url
from . import views
from exchange_app.views import (
    get_exchange_rate_for_currency,
    get_exchange_rate_for_date,
    get_last_exchange_rate_for_currency,
)


urlpatterns = [
    url(
        r"^api/exchange_rates/all/(?P<currency_shortcut>[A-Z]{3})$",
        get_exchange_rate_for_currency,
        name="get_exchange_rate_for_currency",
    ),
    url(
        r"^api/exchange_rates/(?P<currency_shortcut>[A-Z]{3})$",
        get_last_exchange_rate_for_currency,
        name="get_last_exchange_rate_for_currency",
    ),
    url(
        r"^api/exchange_rates/(?P<given_date>[0-9]{4}-[0-9]{2}-[0-9]{2})$",
        get_exchange_rate_for_date,
        name="get_exchange_rate_for_date",
    ),
]
