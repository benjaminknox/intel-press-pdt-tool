import os,mimetypes
from uuid import uuid4
from django.db.models import Q
from topic_management.forms import TopicForm, upload_document_form
from pdtresources.handles import handle_uploaded_file
from pdtresources.templates import form_modal
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse
from topic_management.models import Topic, Document, Comment
from pdtresources.comments import recursive_comments, comment_form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test


#This is the authentication library.
@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='Supervisor') | Q(name='Program Manager')).count() != 0)
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
		topic = Topic(
									name=topic_name,
									description=topic_description,
									user=topic_user)
		topic.save()

		#Get the files
		files = request.FILES

		for name,f in files.iteritems():

			#Single file upload
			#Get the file
			name = f.name
			fileName = "%s-%s" % (uuid4(),name)
			location = '/uploads/%s' % fileName
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
		return redirect('/viewtopic/?publicid=%s#added' % topic.publicid)

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
		'title': 'View Topics'
	}

	#Check to see if the user has filtered 
	#	the topics.
	if 'search' in request.GET:
		#Get the user defined search filter
		search = request.GET['search']
		#Filter the topic list based on the users filtered information.
		topics_list = Topic.objects.filter(name__icontains=search,deleted=False)
	else:
		#Load the topic objects into a list
		topics_list = Topic.objects.filter(deleted=False)

	#Put the topics into a paginator object
	paginator = Paginator(topics_list, 5) # Show 5 documents per page
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

	#Create the query
	queries_without_page = request.GET.copy()

	if queries_without_page.has_key('page'):
		del queries_without_page['page']

	context['queries'] = queries_without_page


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
	#If true a Toastr notification for comments will be shown.
	commentnotification = False
	#If a topic has been approved.
	releasednotification = False
	#If a document has been updated.
	updatednotification = False
	#If a document has been added.
	addednotification = False
	#If a document has been deleted.
	deleteddocumentdnotification = False
	#Add a variable to check if the user owns the topic
	user_is_owner = False

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


		if 'topic_release_id' in request.POST:
			topic_object.readyforr

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

				#Get the old file and delete.
				old_file_path = updated_document.values()[0]['location']

				try:
					#Delete the old file.
					os.remove(old_file_path)
				except OSError:
					print "deleted file not found, but it doesn't really matter"

				#Get the uploaded file.
				f = request.FILES['file']

				#Single file upload
				#Get the file
				name = f.name
				fileName = "%s-%s" % (uuid4(),name)
				location = '/uploads/%s' % fileName
				fileSize = f.size

				updated_document.update(location=location,name=name,fileName=fileName,size=fileSize)
 
				handle_uploaded_file(f,location)

				#Updated notification
				updatednotification = True

		#We have an updated document.
		if 'deleted_documentid' in request.POST:

			#Get the updated document
			deleted_document = topic_object.documents.filter(publicid=request.POST['deleted_documentid'])
			#Get the document
			if deleted_document.exists():

				#Get the old file and delete.
				file_path = deleted_document.values()[0]['location']

				try:
					#Delete the file
					os.remove(file_path)
				except OSError:
					print "deleted file not found, but it doesn't really matter"

				#Remove the m2m relationship.
				topic_object.documents.remove(deleted_document.values()[0]['id'])
				#Delete the document.
				deleted_document.delete()
				#Delete the document notification.
				deleteddocumentdnotification = True


		#We have added a document.
		if 'add_document' in request.POST:

			#Get the uploaded file.
			f = request.FILES['file']

			#Single file upload
			#Get the file
			name = f.name
			fileName = "%s-%s" % (uuid4(),name)
			location = '/home/programmer/upload_dir/%s' % fileName
			fileSize = f.size
			#This is the newdocument.
			newdocument = Document(topic=topic_object,location=location,name=name,fileName=fileName,size=fileSize)
			newdocument.save()
			#Add the document to the topic.
			topic_object.documents.add(newdocument)
			#Upload the file
			handle_uploaded_file(f,location)
			#Updated notification
			addednotification = True

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
		#Add this document.
	  'add_document':form_modal(request,
														'add_document',
														upload_document_form().as_table(),
														'Add a document to the topic',
														multipart=True,
														modal_id="add_document",
														formname_value='add a document',
														action=request.get_full_path(),
														submit_text='upload'
														),
	}

	#Get all of the documents with their comments. 
	documents = [
		#Get all of the documents.
		{'document_object':document,

		 'update_document_form':form_modal(request,
																			'updated_documentid',
																			upload_document_form().as_table(),
																			'Upload a Revised Document',
																			multipart=True,
																			modal_id="update_document_"+document.publicid,
																			formname_value=document.publicid,
																			action=request.get_full_path()
																			),
		 'deleted_document_form':form_modal(request,
																			'deleted_documentid',
																			"You will delete '%s'"%document.name,
																			'Are you sure?',
																			modal_id="deleted_document_"+document.publicid,
																			formname_value=document.publicid,
																			action=request.get_full_path(),
																			submit_text="Yes",
																			submit_button_class="btn-danger",
																			close_button_text='Cancel',
																			close_button_class='pull-right margin-left-10'
																			),
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

	#Check to see if the user owns the topic
	if topic_object.user.id == request.user.id:
		user_is_owner = True

	context= {
		'title':'View Topic',
		'topic': topic,
		'documents': documents,
		'commentnotification': commentnotification,
		'releasednotification' : releasednotification,
		'updatednotification' : updatednotification,
		'deleteddocumentdnotification' : deleteddocumentdnotification,
		'addednotification' : addednotification,
		'user_is_owner' : user_is_owner,
	}

	return render(request,
		'topic_management/viewtopic.html',
		context)

@login_required
def download(request,fileName):
	
	filepath = "/uploads/%s" % fileName

	f = open(filepath,"r")
	mimetype = mimetypes.guess_type(filepath)[0]

	if not mimetype: mimetype = "application/octet-stream"

	response = HttpResponse(f.read(),mimetype=mimetype)
	response["Content-Disposition"] =  "attachment; filename=%s" % os.path.split(filepath)[1]

	return response