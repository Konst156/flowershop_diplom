import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowershop.settings')

app = Celery('flowershop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
