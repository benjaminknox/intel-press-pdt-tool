from django.db import models
from topic_management.models import Topic
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField

# This is the schedule
class ScheduleItem(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	# This is the time this item is
	#		scheduled to start
	#starttime = models.TimeField()
	length = models.IntegerField(default=15)

	# Get the topic of this item.
	topic = models.ForeignKey(Topic)

	#The user who created it.
	presenter = models.ForeignKey(User)

	#The type of review we will do.
	reviewtype = models.CharField(max_length=255)

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)
