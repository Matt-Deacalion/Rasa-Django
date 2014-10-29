"""
WSGI config for rasa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
http://serk.io/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
