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
print(f"Current working directory: {os.getcwd()}")
print(f"Using Python interpreter: {sys.executable}")
load_dotenv("../.env")
print("==========================================================================")
print(f"Loaded ENVIRONMENT: {os.getenv('ENVIRONMENT')}") 
print(f"Loaded DJANGO_SECRET_KEY: {os.getenv('DJANGO_SECRET_KEY')}") 
print(f"Loaded EMAIL_HOST_USER: {os.getenv('EMAIL_HOST_USER')}") 
print(f"Loaded EMAIL_HOST_PASSWORD: {os.getenv('EMAIL_HOST_PASSWORD')}") 
print(f"Loaded ALLOWED_HOSTS: {os.getenv('ALLOWED_HOSTS')}")
ENV=os.getenv('ENVIRONMENT')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"mysite.settings.{ENV}")
print(f"Using Python interpreter: {sys.executable}")

application = get_wsgi_application()
