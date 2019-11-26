from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=3)
    usd_price = models.DecimalField(decimal_places=2, max_digits=10)


def currency_converter(main_currency: Currency, target_currency: Currency):
    return target_currency.usd_price / main_currency.usd_price
