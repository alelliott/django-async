import os
import django
from channels.routing import get_default_application

from .settings.base import ENV

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{project_name}}.settings.{}".format(ENV))
django.setup()
application = get_default_application()
