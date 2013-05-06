from django.db import models
from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User, Group, Permission

"""
" Extendeduser model
"	This  model extends the user information,
"		rather than modifying the User class
"		in the Auth library just create a table
"		related to it.
"""
class Extendeduser(models.Model):
	#User relationship
	user = models.OneToOneField(User)
	notifications = models.ManyToManyField('Notification')

"""
" Document class.
"	This is an uploaded document:
"		-has many `File`
"		-has many `Comment`
"		-has a User
"""
class Document(models.Model):

	#The name of the document
	name = models.CharField(max_length=255)

	#Returns the value of the document name
	#	for reference purposes. 
	def __unicode__(self):
		return self.name

    #A short description of the document
    #	written by the uploader.
	description = models.TextField()

	#This creates the `file` relationship
	file = models.ManyToManyField('File')

	#The user
	user = models.ForeignKey(User)

	#This creates the `Comment` relationship
	comments = models.ManyToManyField('Comment',blank=True)

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

"""
" File class.
"	-has many Comment.
"	-has a Document.
"	TODO: Lookup file security.
"	TODO: Figure out how to use the UUID django-extension.
"""
class File(models.Model):
	
	#The location of the file on the hard disk.
	location = models.CharField(max_length=255)
	
	#The name of the file for display purposes.
	filename = models.CharField(max_length=255)

	#Returns the value of the filename
	#	for reference purposes. 
	def __unicode__(self):
   			return self.filename

	#The Check Sum for the file.
	checksum = models.CharField(max_length=255)

	#The UUID field for the file.
	uuid = UUIDField(version=4)

	#The size of the file.
	size = models.IntegerField()

	#The documentid.
	documentid = models.ForeignKey('Document',related_name='_file')    
    
    #The collection of comments attributed to this file.
	comments = models.ManyToManyField('Comment',blank=True)

    #The date the row is created.
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row.
	lastmodified = models.DateTimeField(auto_now=True)

"""
" Meeting class
"	-has many Document.
"	-has a User.
"""
class Meeting(models.Model):

	#The collection of documents attributed to this meeting.
	documents = models.ManyToManyField('Document')

	#The user that added it
	added_user = models.ForeignKey(User)

	#The name of the meeting
	name = models.CharField(max_length=255)

	#The Description of the meeting
	description = models.TextField()

	#The date the meeting starts.
	start_date = models.DateTimeField()

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

"""
" Notification class
"	-has a User.
"""
class Notification(models.Model): 
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

	#These are reasons for a user to be notified
	NULL_NOTIFICATION = None
	NEW_DOCUMENT = 'new_doc'
	NEW_COMMENT = 'new_comment' 
	REASON_FOR_NOTIFICATION = (
		(NULL_NOTIFICATION,None),
		(NEW_DOCUMENT,'New Document'),
		(NEW_COMMENT, 'New Comment'),
	)
	#Predefined choices are in REASON_FOR_NOTIFICATION
	reason = models.CharField(max_length=255,
						  	  choices=REASON_FOR_NOTIFICATION,
							  default=NULL_NOTIFICATION)

	#The user
	user = models.ForeignKey(User)

	#Flag to let us know if the user has viewed 
	#	the notification.
	viewed = models.BooleanField()

"""
" Organization class
"	-has a User
"""
class Organization(models.Model):


	#The name of the organization
	name = models.CharField(max_length=255)

	#The collection of users in the orginization    
	users = models.ManyToManyField(User)

    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

	#Returns the value of the filename
	#	for reference purposes. 
	def __unicode__(self):
   			return self.name

"""
" Comment class
"	-has a User.
"""
class Comment(models.Model):

	#The user
	user = models.ForeignKey(User)
		
	#The actual content of the comment
	content = models.TextField()
	
	#The actual character field.
	title = models.CharField(max_length=255,blank=True)
	
	#The collection of comments associated with this field
	comments = models.ManyToManyField('Comment',blank=True)

	#Whether or not the model is reported.
	reported = models.BooleanField() 
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
 	
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)