from .base import *
import os
from dotenv import load_dotenv

import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
print(f"Current working directory: {os.getcwd()}")
print(f"Using Python interpreter: {sys.executable}")
load_dotenv("../../.env")
print("==========================================================================")
print(f"Loaded ENVIRONMENT: {os.getenv('ENVIRONMENT')}") 
print(f"Loaded DJANGO_SECRET_KEY: {os.getenv('DJANGO_SECRET_KEY')}") 
print(f"Loaded EMAIL_HOST_USER: {os.getenv('EMAIL_HOST_USER')}") 
print(f"Loaded EMAIL_HOST_PASSWORD: {os.getenv('EMAIL_HOST_PASSWORD')}") 
print(f"Loaded ALLOWED_HOSTS: {os.getenv('ALLOWED_HOSTS')}")
ENV=os.getenv('ENVIRONMENT')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS=tuple(os.getenv('ALLOWED_HOSTS').split(","))

try:
    from .local import *
except ImportError:
    pass
