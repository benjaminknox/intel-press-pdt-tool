from PDTtool import settings
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib.auth.models import User
from meeting_management.models import Meeting
from user_management.models import ExtendedUser
from meeting_management import resources as meetingresources
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from djnotifications import lib as notificationslib
from schedule_management.models import CategorySchedule

def meeting_notification(meeting_pk=None,
                         day_count=None,
                         template_name=None,
                         notification_set=None,
                         notification_day_count=None,
                         subject=None):

  #Run the count down information
  if (not day_count or
      not template_name or
      not notification_set or
      not notification_day_count): 
    print "Not enough information found."
    return False  

  #Get the meeting provided in the notification.
  meeting = Meeting.objects.filter(pk=meeting_pk)
  #Get the schedule objects.
  categoryschedules = CategorySchedule.objects.filter(meeting=meeting)
  
  #Set the from email
  from_email = settings.DEFAULT_FROM_EMAIL

  #Get the count of the meeting.
  if meeting.count() <= 0:
    #Return a message.
    print "No meeting found, the notification will not be sent."
    return False
  else:
    #Get the meeting object.
    meeting = meeting[0]

  if notification_set == settings.NOTIFICATION_SETS['countdown_set']['varname']:
    #Get all of the program managers.
    recipients = ExtendedUser.objects.filter(user__groups__name='Program Manager',
                                             deleted=False,
                                             user__is_active=True)

  #Check 
  elif notification_set == settings.NOTIFICATION_SETS['startdate_set']['varname']:
    recipients = meetingresources.loadattendees(meeting=meeting)
  else:
    #Set a blank list for the recipients
    recipients = []

  #Loop through each of the program managers selected.
  for recipient in recipients:
    #Create a boolean to switch the sending.
    send = True
    #Check that the notifications are turned off.
    if not getattr(recipient.usernotifications,settings.NOTIFICATION_FIELDS['email_notification']['fieldname']):
      send = False

    #Loop through the notifications.
    for name,notification_item in settings.NOTIFICATION_FIELDS.iteritems():
      #Check the notification day count.
      if (
        (
          'notification_day_count' in notification_item and
          notification_item['notification_set']['varname'] == notification_set and
          notification_item['notification_day_count'] == notification_day_count
        )
        or
        (
          'notification_day_count' not in notification_item and
          notification_item['notification_set']['varname'] == notification_set
        )
      ):

        #Get the attribute.
        check = getattr(recipient.usernotifications,notification_item['fieldname'])
        if not check:
          send = False

    if not send:
      print "User turned off the notification"
      break

    #Create some context variables for the email templates.
    context = {
      'user':recipient,
      'meeting':meeting,
      'categoryschedules':categoryschedules,
      'domain_name':settings.DOMAIN_NAME
    }

    #Get the subject.
    #subject = "A cut off date for '%s' is coming up" % (meeting.name)

    #Set the email we are sending to.
    to_email = (recipient.user.email,)

    #Render the text email message.
    text_message = render_to_string(template_name+'.txt',context)
    #Render the html email message.
    html_message = render_to_string(template_name+'.html',context)

    #Create an email object that allows us to send an html message.
    msg = EmailMultiAlternatives(subject,text_message,from_email,to=to_email)
    #Attach the html message to the header.
    msg.attach_alternative(html_message, "text/html")
    #Send the message.
    msg.send()
