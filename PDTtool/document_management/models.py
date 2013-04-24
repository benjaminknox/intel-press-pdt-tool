from django.db import models

"""
" Document class.
"	This is an uploaded document:
"		-has many `File`
"		-has many `Comment`
" 	TODO: Connect to user auth model.
"""
class Document(models.Model):
	
	#The unique id of the row
	id = models.AutoField(primary_key=True)
	
	#The name of the document
	name = models.CharField(max_length=255)

	#Returns the value of the document name
	#	for reference purposes. 
	def __unicode__(self):
		return self.name

    #A short description of the document
    #	written by the uploader
	description = models.TextField()

	#This creates the `Comment` relationship
	comments = models.ManyToManyField('Comment')

	#This creates the `file` relationship
	file = models.ManyToManyField('File')    
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

"""
" File class.
"	TODO: Lookup file security.
"   TODO: Finish Class Definition.
"	TODO: Figure out how to use the UUID django-extension.
"""
class File(models.Model):

	#The unique id of the row
	id = models.AutoField(primary_key=True)
	
	#The location of the file on the hard disk
	location = models.CharField(max_length=255)
	
	#The name of the file for display purposes
	filename = models.CharField(max_length=255)

	#Returns the value of the filename
	#	for reference purposes. 
	def __unicode__(self):
   			return self.filename

	size = models.IntegerField()
	documentid = models.ForeignKey('Document',related_name='_file')    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)
	comments = models.ManyToManyField('Comment')

"""
" Meeting class
"	TODO: Add a user field.
"""
class Meeting(models.Model):
	#The unique id of the row
	id = models.AutoField(primary_key=True)    
	documents = models.ManyToManyField('Document')    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

"""
" Notification class
"	TODO: Add a user feild.
"""
class Notification(models.Model):
	#The unique id of the row
	id = models.AutoField(primary_key=True)    
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

	#Flag to let us know if the user has viewed 
	#	the notification.
	viewed = models.BooleanField()

"""
" Organization class
"""
class Organization(models.Model):
	#The unique id of the row
	id = models.AutoField(primary_key=True)    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)

"""
" Comment class
"""
class Comment(models.Model):
	#The unique id of the row
	id = models.AutoField(primary_key=True)    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)
	comments = models.ManyToManyField('Comment')