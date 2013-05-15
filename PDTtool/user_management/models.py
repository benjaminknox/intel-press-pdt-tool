from django.db import models
from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User

# This model is ment to extend the default user auth
#		in the model class.
class ExtendedUser(models.Model):

	class Meta:
		ordering = ['pk']

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#Get the user
	user = models.OneToOneField(User)

	#Create a collection of notifications.
	notifications = models.ManyToManyField('Notification',blank=True)

	#The phone number for the user.
	phonenumber = models.CharField(max_length = 255)

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

# This model is for notifications in the system
#		for things like uploaded documents, 
#		or comments on documents.
class Notification(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#The name of the field.
	name = models.CharField(max_length=255)
	#The reason for the notification.
	reason = models.TextField(blank=True)
	#This is the unicode value.
	def __unicode__(self):
		return self.reason
	#Wether or not it has been viewed.
	viewed = models.BooleanField()

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

# This model attributes a collection of users to an
#		 organization.
class Organization(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#The collection of users.
	users = models.OneToOneField(User)
	#The name of the organization
	name = models.CharField(max_length=255)
	#This is the unicode value.
	def __unicode__(self):
		return self.name

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

# This model is the record for activating a user.
#		The publicid is stored and when a user clicks on a
#			link sent to their email they get activated
#			and the record is removed from the database.
class ActivateUserDB(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#The user.
	user = models.OneToOneField(User)

	#This is the unicode value.
	def __unicode__(self):
		return self.publicid

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

# This model is the record for a password reset form.
#		The publicid is stored and when a user clicks on a
#			link sent to their email the password gets
#			reset.
class ForgotPasswordDB(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#The user.
	user = models.OneToOneField(User)

	#This is the unicode value.
	def __unicode__(self):
		return self.publicid

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)
