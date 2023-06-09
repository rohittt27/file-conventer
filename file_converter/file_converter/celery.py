# from celery import Celery
# import os

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')

'''
for local
'''
# import os
# from celery import Celery

# # setting the Django settings module.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')
# app = Celery('file_converter')
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Looks up for task modules in Django applications and loads them
# app.autodiscover_tasks()


'''
for docker
'''

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_converter.settings')

app = Celery('file_converter')

# Update the broker URL to use Redis container's hostname or IP address
app.conf.broker_url = 'redis://redis:6379/0'

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')