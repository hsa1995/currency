import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_project.settings')

app = Celery('currency_project')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-rates-every-day': {
        'task': 'core.tasks.update_rates',
        'schedule': crontab(),
    },
}
