"""
WSGI config for GeoGamesMedieval project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GeoGamesMedieval.settings')
application = get_wsgi_application()