from django.db import models

"""
Maybe there should be a different data structure implemented, 
but I thought that there is no need at this point to make relations because there is finite amoutn of currencies. 
"""


class ExchangeRate(models.Model):
    """
    ExchangeRate Model
    Defines the attributes of a single ExchangeRate row in database.
    """

    exchange_rate = models.DecimalField(decimal_places=8, max_digits=16)
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    date = models.DateField()
