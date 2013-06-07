from djnotifications import lib
from celery.task.schedules import crontab  
from celery.decorators import periodic_task
from djnotifications.models import Notification

#########################
# Check the notifications
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))  
def check_notifications(*args,**kwargs):
  #Get all of the notifications.
  notifications = Notification.objects.filter(deleted=False)
  #Count the notifications if any exist run them.
  if len(notifications) > 0:
    print "There are waiting notifications in the queue."
    #Loop through each task in the database.
    for notification in notifications:
      #Run the task.
      lib.run_notification(notification)
      
  #If there are no new notifications.
  else:
    print "No new notifications."
