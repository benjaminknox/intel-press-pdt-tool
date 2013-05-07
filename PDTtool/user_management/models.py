from django.db import models
from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User, Group, Permission

# This model is ment to extend the default user auth
#		in the model class.
class ExtendedUser(models.Model):
	#Get the user
	user = models.OneToOneField(User)
	#Create a collection of notifications.
	Notifications = models.ManyToManyField('Notification')

# This model is for notifications in the system 
#		for things like uploaded documents, 
#		or comments on documents.
class Notification(models.Model):
	#The name of the field.
	name = models.CharField(max_length=255)
	#The reason for the notification.
	reason = models.TextField()
	#Wether or not it has been viewed.
	viewed = models.BooleanField()

# This model attributes a collection of users to an
#		 organization.
class Organization(models.Model):
	#The collection of users.
	users = models.OneToOneField(User)
	#The name of the organization
	name = models.CharField(max_length=255)