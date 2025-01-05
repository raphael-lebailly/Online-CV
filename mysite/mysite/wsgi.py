"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
load_dotenv("../.env")

ENV=os.getenv('ENVIRONMENT')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"mysite.settings.{ENV}")

application = get_wsgi_application()
