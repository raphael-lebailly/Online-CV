from .base import *
import os
from dotenv import load_dotenv

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
