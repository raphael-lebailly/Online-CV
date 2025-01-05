#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('./.env')
ENV=os.getenv('ENVIRONMENT')

current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"mysite.settings.{ENV}")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
