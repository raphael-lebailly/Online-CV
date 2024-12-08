#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
ENV=os.getenv('ENVIRONMENT')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"mysite.settings.{ENV}")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
