from django.db import models
from topic_management.models import Topic
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField
from schedule_management.models import ScheduleItem

# This is the meeting created by a supervisor.
class Meeting(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#name
	name = models.CharField(max_length=255)

	#description
	description = models.TextField()

	#This is the duedate.
	duedate = models.DateTimeField()

	#The maximum number of ScheduleItems.
	maxscheduleitems = models.IntegerField()

	#This is the date and time it starts.
	startdate = models.DateTimeField()

	#Collection of the users attending.
	#usersattending = models.ManyToManyField(User,related_name='usersattending')

	#This is the user created.
	user = models.ForeignKey(User,related_name='createduser')

	#The duration in minutes
	duration = models.IntegerField()

	#This is a collection of items.
	#scheduleitems = models.ForeignKey(ScheduleItem)
	topics = models.ManyToManyField(Topic)

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)