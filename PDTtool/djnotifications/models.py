from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField

#################################
# This is the model notification.
class Notification(models.Model):

  def __unicode__(self):
    return "%s.%s %s to %s at %s" % (self.modulename,
                                     self.task,
                                     self.message, 
                                     self.user.get_full_name(),
                                     self.time_of_notification)

  ##############
  #The publicid.
  publicid = UUIDField(version=4, unique=True)

  ################################################################
  #The module, this allows to add a module to any of the packages
  #   on the path so we can add notifications to the
  modulename = models.CharField(max_length=400)

  ###############################################
  #The task is a function name within the module.
  task = models.CharField(max_length=400)
  
  ##################################
  #The message for the notification.
  message = models.CharField(max_length=255)

  ##################################
  #The user that is being notified.
  user = models.ForeignKey(User, null=True, blank=True)

  ###############################################
  #Determines if this is a timebound notification
  timebound = models.BooleanField(default=True)

  ###################################
  #The time to fire the notification.
  time_of_notification = models.DateTimeField(null=True,blank=True)

  #######################################
  #If this is false the field is deleted.
  deleted = models.BooleanField(default=False)

  #############################
  #The date the row is created.
  created = models.DateTimeField(auto_now_add=True)
    
  ######################################
  #The date of the last edit of the row.
  lastmodified = models.DateTimeField(auto_now=True)

class Notification_settings(models.Model):

  ##############
  #The publicid.
  publicid = UUIDField(version=4, unique=True)

  ##################
  #The notification.
  notification = models.ForeignKey(Notification)

  ##############################
  #The user of the notification.
  user = models.ForeignKey(User)

  ######################################################
  #Boolean for sending the notification to email or not.
  sendemail = models.BooleanField(default=True)

  ###################################
  #Boolean for notifying on the page.
  notify = models.BooleanField(default=True)

  ############################
  #The date the row is created
  created = models.DateTimeField(auto_now_add=True)
    
  #####################################
  #The date of the last edit of the row
  lastmodified = models.DateTimeField(auto_now=True)

#######################################
# These are arguments for the function.
class Task_argument(models.Model):

  ##############
  #The publicid.
  publicid = UUIDField(version=4, unique=True)

  #############################################
  #This is the notification that it belongs to.
  notification = models.ForeignKey(Notification)

  ##########################
  #The argument keyword name
  argument_keyword_name = models.CharField(max_length=255)

  ###########################
  #The argument keyword value
  argument_keyword_value = models.CharField(max_length=255)

  #######################################
  #If this is false the field is deleted.
  deleted = models.BooleanField(default=False)

  ############################
  #The date the row is created
  created = models.DateTimeField(auto_now_add=True)
    
  #####################################
  #The date of the last edit of the row
  lastmodified = models.DateTimeField(auto_now=True)