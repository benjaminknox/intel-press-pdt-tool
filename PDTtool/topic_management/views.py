import os
from topic_management.forms import TopicForm
from django.shortcuts import render, redirect
from pdtresources.handles import handle_uploaded_file
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from topic_management.models import Topic, Document, Comment
from pdtresources.comments import recursive_comments, comment_form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from uuid import uuid4

#This is the authentication library.
@login_required
def addtopic(request):
	
	context= {
			'title':'Add Topic',
	}

	#Check for POST data.
	if request.method == 'POST':
		#Get the document post data
		topic_name = request.POST['name']
		topic_description = request.POST['description']
		topic_user = request.user
		#Create a new Document and save it.
		topic = Topic(name=topic_name, description=topic_description,user=topic_user)
		topic.save()

		#Get the files
		files = request.FILES

		for name,f in files.iteritems():

			#Single file upload
			#Get the file
			name = f.name
			fileName = "%s-%s" % (uuid4(),name)
			location = '/home/programmer/upload_dir/%s' % fileName
			fileSize = f.size

			#Load a new uploaded file and save it.
			uploadedfile = Document(topic=topic,
								location = location,
							    name=name,
							    fileName=fileName,
							    size=fileSize)
			uploadedfile.save()

			#Save the file on to the directory.
			handle_uploaded_file(f,location)

			topic.documents.add(uploadedfile)

		#Return the redirect.
		return redirect('/viewtopics/#added')

	else:
		#Create an unbound post data.
		topicform = TopicForm

	#Make a context variable
	#	for the topicform.
	context['topicform'] = topicform

	return render(request,
					'topic_management/addtopic.html',
					context)

# This is a list of the topics.
@login_required
def viewtopics(request):

	context = {
		'title': 'View Topic'
	}

	#Check to see if the user has filtered 
	#	the topics.
	if request.method == 'POST':
		#Get the user defined search filter
		search = request.POST['search']
		#Filter the topic list based on the users filtered information.
		topics_list = Topic.objects.filter(name__icontains=search,deleted=False)
	else:
		#Load the topic objects into a list
		topics_list = Topic.objects.filter(deleted=False)

	#Put the topics into a paginator object
	paginator = Paginator(topics_list, 10) # Show 25 documents per page
	#Get the page
	page = request.GET.get('page')

	#This block of code tries loading into a paginator object.
	try:
		#Load the documents for this page.
		topics = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		topics = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		topics = paginator.page(paginator.num_pages)

	#Stor the topics.
	context['topics'] = topics
	
	return render(request,
			'topic_management/viewtopics.html',
			context)

# View the file.
@login_required
def viewtopic(request):

	#If there is no topic.
	notopic = True
	#If true a Toastr notification for comments will be added.
	commentnotification = False
	#If a document has been approved
	releasednotification = False
	#If a document has been updated
	updatednotification = False

	#Get the public id of the topic.
	if 'publicid' in request.GET:
		#This is the publicid.
		publicid = request.GET['publicid']
		try:
			#Check for a topic.
			topic_object = Topic.objects.get(publicid=publicid,deleted=False)
			notopic=False
		except ObjectDoesNotExist:
			#If the topic does not exist.
			notopic=True

	#If there is no topic.
	if notopic:
		#Redirect if the topic is not found
		#		to the list of topics.
		return redirect('/viewtopics/')

	#Check for POST data
	if request.method == 'POST':

		#We deleted the topic.
		if 'deleted_topicid' in request.POST and request.POST['deleted_topicid'] == topic_object.publicid:
			#Delete the topic object
			topic_object.deleted = True
			topic_object.save()

			#Redirect to the list of topics, there is a hash
			#		for a notification.
			return redirect('/viewtopics/#deleted')

		#We approved the document.
		if 'released_topicid' in request.POST and request.POST['released_topicid'] == topic_object.publicid:
			releasednotification = True

		#We have an updated document.
		if 'updated_documentid' in request.POST:

			#Get the updated document
			updated_document = topic_object.documents.filter(publicid=request.POST['updated_documentid'])
			#Get the document
			if updated_document.exists():

				old_file_path = updated_document.values()[0]['location']

				os.remove(old_file_path)

				#Get the uploaded file.
				f = request.FILES['file']

				#Single file upload
				#Get the file
				name = f.name
				fileName = "%s-%s" % (uuid4(),name)
				location = '/home/programmer/upload_dir/%s' % fileName
				fileSize = f.size

				updated_document.update(location=location,name=name,fileName=fileName,size=fileSize)
 
				handle_uploaded_file(f,location)

				#Updated notification
				updatednotification = True

		"""
		" The following adds comments to the specified object
		"""
		#Add a comment to the topic
		if 'topicid' in request.POST and request.POST['topicid'] == topic_object.publicid:
			content = request.POST['content']

			newcomment = Comment(user=request.user,content=content)
			newcomment.save()

			topic_object.comments.add(newcomment)

			commentnotification = True

		#Assumes the document exists.
		#Add a comment to the document
		if 'documentid' in request.POST:

			documentid = request.POST['documentid']

			document_object = Document.objects.get(publicid=documentid)

			content = request.POST['content']
			
			newcomment = Comment(user=request.user,content=content)
			newcomment.save()
			
			document_object.comments.add(newcomment)

			commentnotification = True

		#Assumes the comment exists.
		#Add a reply to the comment.
		if 'commentid' in request.POST:

			commentid = request.POST['commentid']

			comment_object = Comment.objects.get(publicid=commentid)

			content = request.POST['content']
			
			newcomment = Comment(user=request.user,content=content)
			newcomment.save()
			
			comment_object.comments.add(newcomment)

			commentnotification = True

		"""
		" End the logic to add comments.
		"""

	#Get the topic
	topic = {
		#Store the topic_object
		'topic_object':topic_object,
		#Get the comments
		'comments':[
			#Get the comments for the topic
			{'html':str(recursive_comments(request, comment.publicid))}
			#Run a loop on the comments.
			for comment in topic_object.comments.all() 
		],
		#Get the comment form for the topic.
		'comment_form':comment_form(request,'topic',topic_object.publicid),
	}

	#Get all of the documents with their comments. 
	documents = [
		#Get all of the documents.
		{'document_object':document,
		 #Get the comments.
		 'comments':[
		 	#Get the comments for each document.
			{'html':str(recursive_comments(request, comment.publicid))}
			#Run a loop on the comments.
			for comment in document.comments.all()
		],
		'comment_form':comment_form(request,'document',document.publicid),
		}
		#Run a loop on the documents
		for document in topic_object.documents.all()
	]

	context= {
			'title':'View Topic',
			'topic': topic,
			'documents': documents,
			'commentnotification': commentnotification,
			'releasednotification' : releasednotification,
			'updatednotification' : updatednotification,
	}

	return render(request,
		'topic_management/viewtopic.html',
		context)