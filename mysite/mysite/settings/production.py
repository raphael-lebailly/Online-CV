from .base import *
import os
from dotenv import load_dotenv

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#]
#STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

current_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_dir)
load_dotenv("../../.env")
ENV=os.getenv('ENVIRONMENT')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS=tuple(os.getenv('ALLOWED_HOSTS').split(","))

try:
    from .local import *
except ImportError:
    pass
