from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from .settings.base import ENV
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{project_name}}.settings.{}'.format(ENV))

app = Celery('{{project_name}}')

# Apply all configuration keys with defined namespace (CELERY)
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load tasks from all registered apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
