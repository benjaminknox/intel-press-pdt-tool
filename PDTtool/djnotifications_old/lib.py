import sys
import importlib
from django.utils import timezone
from django.core.mail import send_mail
from datetime import timedelta, datetime
from djnotifications.models import Notification,Task_argument

####################
# Run a notification
def run_notification(notification):

  # Get the task message.
  message = notification.message
  # Get the task user. 
  user = notification.user
  #Get the module name, this module
  #   must be on the path.
  modulename = notification.modulename
  #Get the task name.
  task_name = notification.task
  #Get the task arguments.
  arguments_list = Task_argument.objects.filter(notification=notification)
  #Get the arguments.
  arguments = {}
  #Loop through the arguments list.
  for argument in arguments_list:
    #Assign arguments to a dictionary.
    arguments[argument.argument_keyword_name] = argument.argument_keyword_value
  #Get the time of the event.
  time_of_notification = notification.time_of_notification
  #Get the current time.
  now = timezone.now()

  #Compare if the time is less that 
  if time_of_notification <= now:
    #Print the module name
    print modulename+'.'+task_name+' exists.'
    #Import the module.
    importlib.import_module(modulename)
    #Make the module available to 
    #   be used by the system.
    module = sys.modules[modulename]
    #Check if the task exists in the
    #   module that is loaded.
    if hasattr(module,task_name):
      #Get the task to be done.
      task = getattr(module, task_name)
      #Get the task.
      task(**arguments)
      #Delete the task
      notification.deleted = True
      #Save the notification
      notification.save()
    else:
      #The method doesn't exist.
      print 'No method '+module+'.'+task_name

def list_notifications():
  #Get all of the notifications.
  notifications = Notification.objects.filter(deleted=False)
  #Loop through each task in the database.
  for notification in notifications:
    print "%s.%s: %s | %s" % (notification.modulename,notification.task,notification.message,notification.time_of_notification)

def create_notification(modulename="notifications",
                        task="default_task",
                        message="Send a message to a user",
                        user=False,
                        time_of_notification=timezone.now(),
                        arguments={'string':'Hello World','punct':'!!!!'}):

  #If there is no user we have to return false.
  if not user:
    #Get the user.
    user = None

  #Create a new notification.
  notification = Notification(modulename=modulename,
                              task=task,
                              message=message,
                              user=user,
                              time_of_notification=time_of_notification)

  #Save the notification.
  notification.save()

  #Module name.
  for keyword_name,keyword_value in arguments.iteritems():
    #Create the argument keywords.
    task_argument = Task_argument(notification=notification,
                                  argument_keyword_name=keyword_name,
                                  argument_keyword_value=keyword_value)
    #This is the task argument.
    task_argument.save()

def generic_email(from_email="the.pdt.portal@gmail.com",
                  to_email="ben.knox@cummings-inc.com",
                  company="Default Company",
                  name="Default Name",):

  to_email = to_email.split(',')
  
  subject = "%s, you have been notified." % name

  message = "Hi %s,\r\n You are in the company %s." % (name, company)

  #Send the email.
  send_mail(subject, message, from_email, to_email, fail_silently=False)  

#A generic incremental Time bound notification generator.
def time_bound_notifications(event=timezone.now(),
                            day_increments=(1,3,6,7,),
                            modulename="djnotifications.lib",
                            task="generic_email",
                            message="Message a user at increments",
                            arguments={
                              'name':'Default Name',
                              'to_email':'ben.knox@cummings-inc.com',
                              'company':'Default company',
                            }):

  if not timezone.is_aware(event):
    event = timezone.make_aware(event, timezone.get_default_timezone())

  today = timezone.make_aware(datetime.now(),timezone.get_default_timezone())

  for increment in day_increments:

    time_of_notification = event - timedelta(days=increment)

    if today.date() <= time_of_notification.date():
      create_notification(modulename=modulename,
                          task=task,
                          message=message,
                          user=False,
                          time_of_notification=time_of_notification,
                          arguments=arguments)