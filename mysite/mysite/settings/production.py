from .base import *
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS=tuple(os.getenv('ALLOWED_HOSTS').split(","))

try:
    from .local import *
except ImportError:
    pass
