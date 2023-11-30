import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myceleryproject.settings')

app = Celery('myceleryproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule ={
    'every-10-seconds':{
        'task':'myapp.task.clear_session_cache',
        'schedule':10, #when want to schedule using timedelta then import time and thenafter "'schedule':timedelta('seconds'=10)"
        'args':('11111', )
    }
}

@app.task
def add(x,y):
    # sleep(20)
    return x+y
# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
