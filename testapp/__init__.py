# flake8: noqa
import django
django.setup()

from django.core.management import call_command
call_command('migrate')
