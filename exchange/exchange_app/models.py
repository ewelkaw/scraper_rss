from django.db import models


class Currency(models.Model):
    """
    Curriencies Model
    Defines the pairs of base and target currency.
    """

    base_currency = models.CharField(max_length=3, null=False)
    target_currency = models.CharField(max_length=3, null=False)

    class Meta:
        unique_together = ("base_currency", "target_currency")

    def __str__(self):
        return f"{self.base_currency}/{self.target_currency}"


class ExchangeRate(models.Model):
    """
    ExchangeRate Model
    Defines the attributes of a single ExchangeRate row in database.
    """

    exchange_rate = models.DecimalField(decimal_places=8, max_digits=16)
    currency = models.ForeignKey(
        Currency, related_name="currency", on_delete=models.CASCADE, null=False
    )
    date = models.DateField()

    def __str__(self):
        return f"exchange rate value {self.exchange_rate}|{self.date}"

