from djnotifications import lib
from celery.task.schedules import crontab  
from celery.decorators import periodic_task
from djnotifications.models import Notification

#########################
# Check the notifications
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def check_count_down_dates(*args,**kwargs):
  '''
  Go through all due dates and check if they are:
    -1 week away
    -3 days away
    -2 days away
    -1 day away
  '''
  