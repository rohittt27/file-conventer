# from celery import Celery
# import os

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')


import os
from celery import Celery

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')
app = Celery('file_converter')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()