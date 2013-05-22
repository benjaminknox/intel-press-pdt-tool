from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField

# The Topic is an subject that is to be reviewed 
#		by the Program Manager, it has many 
#		documents and comments.
class Topic(models.Model):

	#Class Meta
	class Meta:
		ordering = ['pk']

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#Name of the topic.
	name = models.CharField(max_length=255)

	#Define the name
	def __unicode__(self):
		return self.name

	#The description of the topic.
	description = models.TextField()

	#Collection of Documents.
	documents = models.ManyToManyField('Document',related_name='topic_documents')

	#A flag for ready for review
	readyforreview = models.BooleanField(default=False)

	#A time in minutes for presenting.
	presentationlength = models.IntegerField(default=0)

	#The user who created it.
	user = models.ForeignKey(User)

	#Collection of Comments.
	comments = models.ManyToManyField('Comment')

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)


# These are the documents that are uploaded
#		to the documents.
class Document(models.Model):

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#The topic it belongs to
	topic = models.ForeignKey(Topic, related_name='document_topic')

	#The location on the hard disk.
	location = models.CharField(max_length=255)

	#The name of the file.
	name = models.CharField(max_length=255)

	#Filename get the filename.
	fileName = models.CharField(max_length=255)

	#The size of the file when uploaded.
	size = models.IntegerField()

	#The checksum generated for security.
	checksum = models.CharField(max_length=255)

	#Collection of comments.
	comments = models.ManyToManyField('Comment',blank=True)

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)


# This is a comment, it is the feedback on a
#		topic, document, or comment.
class Comment(models.Model):
	
	class Meta:
		ordering = ['pk']

	#The publicid.
	publicid = UUIDField(version=4, unique=True)

	#The user who created it.
	user = models.ForeignKey(User)

	#The description of the topic.
	content = models.TextField()

	#Collection of comments.
	comments = models.ManyToManyField('Comment',blank=True)

	#Boolean for a reported value
	reported = models.BooleanField(default=False)

	#If this is false the field is deleted.
	deleted = models.BooleanField(default=False)
    
    #The date the row is created
	created = models.DateTimeField(auto_now_add=True)
    
    #The date of the last edit of the row
	lastmodified = models.DateTimeField(auto_now=True)