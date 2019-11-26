from datetime import datetime

from forex_python.converter import CurrencyRates

from currency_project.celery import app
from core.models import Currency


@app.task
def update_rates():
    c = CurrencyRates()
    rates = c.get_rates('USD')
    current_rates = Currency.objects.all()

    for currency in current_rates:
        currency.usd_price = rates.get(currency.name)
        currency.save()
    with open('test.txt', 'a+') as test_file:
        test_file.write(str(datetime))
