import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryserver.settings')

app = Celery('celeryserver')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()