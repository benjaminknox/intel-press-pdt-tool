from django.db import models
from topic_management.models import Topic
from django.contrib.auth.models import User
from user_management.models import ExtendedUser
from django_extensions.db.fields import UUIDField
#from schedule_management.models import ScheduleItem

# This is the meeting created by a supervisor.
class Meeting(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#name
	name = models.CharField(max_length=255)

	#Define the name
	def __unicode__(self):
		return self.name
	
	#description
	description = models.TextField()

	#This is the duedate.
	duedate = models.DateField()

	#The maximum number of ScheduleItems.
	maxscheduleitems = models.IntegerField()

	#This is the date and time it starts.
	startdate = models.DateField()

	#This is the time it starts.
	starttime = models.TimeField(blank=True)

	#Collection of the users attending.
	attendees = models.ManyToManyField(ExtendedUser,related_name='attendees')

	#This is the length of the category in the schedule.
	currentlength = models.IntegerField(default=0)

	#This is how much time is left in the meeting.
	timeleft = models.IntegerField(null=True,default=None)

	#This is the user created.
	user = models.ForeignKey(User,related_name='createduser')

	#The duration in minutes
	duration = models.IntegerField()

	#This is a collection of items.
	#scheduleitems = models.ForeignKey(ScheduleItem)
	#topics = models.ManyToManyField(Topic,related_name='_meetingtopics')

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)
    
  #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
  #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

class MeetingChatLine(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#The ExtendedUser user.
	extendeduser = models.ForeignKey(ExtendedUser)

	#The meeting that it belongs to.
	meeting = models.ForeignKey(Meeting)

	#The line
	line = models.TextField(null=False)
  
  #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
  #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)
