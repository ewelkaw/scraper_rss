from django.contrib import admin

from exchange_app.models import ExchangeRate, Currency

# Register your models here.
admin.site.register(ExchangeRate)
admin.site.register(Currency)
