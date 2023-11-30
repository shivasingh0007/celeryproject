from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask,IntervalSchedule
import json


@shared_task(name="Sub_task")
def sub(x,y):
    sleep(20)
    return x-y

@shared_task
def add(x,y):
    sleep(10)
    return x+y

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id

@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared: {key}")
    return key


# Create Schedule every 30 seconds 
schedule, created = IntervalSchedule.objects.get_or_create(every=15,period=IntervalSchedule.SECONDS,)

PeriodicTask.objects.get_or_create(name="Clear New Task",task='myapp.task.clear_task_data',interval=schedule,args=json.dumps(['hello']),)