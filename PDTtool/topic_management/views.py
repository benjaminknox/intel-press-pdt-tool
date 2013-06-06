import os,mimetypes
from uuid import uuid4
from shutil import copyfile
from PDTtool import settings
from datetime import datetime
from django.db.models import Q
from pdtresources.templates import form_modal
from django.core.exceptions import ObjectDoesNotExist
from topic_management.resources import generate_topic_slug
from django.shortcuts import render, redirect, HttpResponse
from topic_management.models import Topic, Document, Comment
from topic_management.forms import TopicForm, upload_document_form
from pdtresources.comments import recursive_comments, comment_form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test
from pdtresources.handles import create_directory, delete_topic, handle_uploaded_file

###
# View addtopic allows a Supervisor or
#		Program Manager add a topic.
###
@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='Supervisor') | Q(name='Program Manager')).count() != 0)
def addtopic(request):

	context= {
			'title':'Add Topic',
	}

	#Check for POST data.
	if request.method == 'POST':

		topicform = TopicForm(request.POST)

		if topicform.is_valid():

			#Get the topic post data
			topic_name = request.POST['name']
			topic_description = request.POST['description']
			topic_category = request.POST['category']
			topic_user = request.user
			topic_slug = generate_topic_slug()
			
			#Create a new topic and save it.
			topic = Topic(
										name=topic_name,
										description=topic_description,
										user=topic_user,
										category=topic_category,
										topic_slug = topic_slug
										)
			topic.save()

			#Create a new directory for the topic.
			directory = create_directory(topic,settings.UPLOADED_TOPIC_DIR)

			#Get the files
			files = request.FILES

			#Thesea re the names of hte files.
			for name,f in files.iteritems():

				#Single file upload
				#Get the file
				name = f.name
				fileName = "%s-%s" % (uuid4(),name)
				#The uploaded_topic_dir is in PDTtool.settings.
				location = '%s/%s' % (directory, fileName)
				#Handle the filesize.
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

###
# View viewtopics is a list of the
#		topics. Any user can access it.
#
#	For the Supervisor or Program Manager
#		to view his own topics a get
#		variable 'mytopics' can be added.
###
@login_required
def viewtopics(request):

	context = {
		'title':'View Topics'
	}

	#Check to see if the user has filtered 
	#	the topics.
	if 'search' in request.GET:
		#Get the user defined search filter
		search = request.GET['search']
		#Filter the topic list based on the users filtered information.
		topics_list = Topic.objects.filter((
			Q(deleted=False) & 
				(Q(name__icontains=search) | 
				 Q(category__icontains=search) |
				 Q(topic_slug__icontains=search) 
			 	)
			))
	else:
		#Load the topic objects into a list
		topics_list = Topic.objects.filter(deleted=False)

	#Check for the mytopics variable 
	#		in the get request.
	if 'mytopics' in request.GET:
		#Filter the topics_list by the current logged in user=Topic.user.
		topics_list = topics_list.filter(user=request.user).order_by('readyforreview', '-supervisor_released')
	else:
		#Update the 
		topics_list = topics_list.order_by('-readyforreview', 'supervisor_released')

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

###
# View viewtopic is a list of the
#		documents uploaded to the
#		for the topic. Any user can
#		access it.
#
#	An owner of a topic has a special
#		gui.
###
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

		#The directory of the location of the documents
		topicdirectory = "%s/%s"% (settings.UPLOADED_TOPIC_DIR, publicid)

		try:
			#Check for a topic.
			topic_object = Topic.objects.get(publicid=publicid,deleted=False)
			notopic = False
		except ObjectDoesNotExist:
			#If the topic does not exist.
			notopic = True

	#If there is no topic.
	if notopic:
		#Redirect if the topic is not found
		#		to the list of topics.
		return redirect('/viewtopics/')


	#Check for POST data
	if request.method == 'POST':

		"""
		" These can only be accessed if a user is the owner or a Supervisor
		"""			
		if topic_object.user == request.user or request.user.groups.filter(Q(name='Supervisor')).count() != 0:

			#Update the description of the topic.
			if 'update_topic_description' in request.POST and topic_object.publicid == request.POST['update_topic_description']:
				#Update the description.
				topic_object.description = request.POST['description']
				#Save the topic_object.
				topic_object.save()
			
			#Ready the topic for review
			topic_ready_for_review_index = 'topic_ready_for_review_id'

			#Check if the topic is ready for review.
			if (
				topic_ready_for_review_index in request.POST and
				request.POST[topic_ready_for_review_index] == topic_object.publicid
				):

				#Update the topic presentation length.
				if 'topic_presentationlength' in request.POST:
					#Set the topic ready for review.
					readyforreview = True
					#Set the presentation length to the length entered.
					presentationlength = int(request.POST['topic_presentationlength'])
					#Add a datetime for the time it was set.
					topic_object.datesetforreview = datetime.now()
				else:
					#The topic is not ready for review.
					readyforreview = False
					#Update the presentationlength.
					presentationlength = 15

				#Set the fields in the database.
				topic_object.readyforreview = readyforreview
				topic_object.presentationlength = presentationlength

				#Save the topic object.
				topic_object.save()

				#Reset the meeting duration.
				if topic_object.meeting:
					#This is the topic_meeting.
					topic_meeting = topic_object.meeting;
					#Set the duration to 0.
					duration = 0
					#Loop through each of the topic in the meeting.
					for t in topic_meeting.topics.all():
						#Increment the duration.
						duration += t.presentationlength

					#Set the meeting duration.
					topic_meeting.duration = duration
					#Save the topic meeting.
					topic_meeting.save()

			#We deleted the topic.
			if 'deleted_topicid' in request.POST and request.POST['deleted_topicid'] == topic_object.publicid:
				#Delete the topic object
				topic_object.deleted = True
				topic_object.save()

				#Move the files to a 'deleted' directory.
				delete_topic(topic_object)

				#Redirect to the list of topics, there is a hash
				#		for a notification.
				return redirect('/viewtopics/?deleted=%s' % topic_object.name)

			#We approved the document.
			if 'released_topicid' in request.POST and request.POST['released_topicid'] == topic_object.publicid:
				#In the topic_object set the supervisor_released true.
				topic_object.supervisor_released = True
				#Save the topic.
				topic_object.save()

				directory = create_directory(topic_object,settings.APPROVED_TOPIC_DIR)

				#Loop throught the document and copy
				#		them to the right directory.
				for document in topic_object.documents.all():

					#Get the approved file.
					approved_file = "%s/%s" % (directory,document.fileName)

					#Make a copy of the file.
					copyfile(document.location, approved_file)

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
					#The uploaded_topic_dir is in PDTtool.settings.
					location = '%s/%s' % (topicdirectory, fileName)
					#Get the file size.
					fileSize = f.size
					#Get the updated document
					updated_document.update(location=location,name=name,fileName=fileName,size=fileSize)
	 				#handle the uploaded file.
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

				#The uploaded_topic_dir is in PDTtool.settings.
				location = '%s/%s' % (topicdirectory, fileName)
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
			#This is the content of a topic
			content = request.POST['content']
			#Create a new comment.
			newcomment = Comment(user=request.user,content=content)
			#Save the comment.
			newcomment.save()
			#Add the comment to the topic.
			topic_object.comments.add(newcomment)
			#Create a variable to notify the user of success.
			commentnotification = True

		#Assumes the document exists.
		#Add a comment to the document
		if 'documentid' in request.POST:
			#This is the publicid of the commented document.
			documentid = request.POST['documentid']
			#Get the document.
			document_object = Document.objects.get(publicid=documentid)
			#Get the content of the comment.
			content = request.POST['content']
			#Create a new comment object.
			newcomment = Comment(user=request.user,content=content)
			#Save the comment.
			newcomment.save()
			#Add the comment to the document.
			document_object.comments.add(newcomment)
			#Create a variable to notify the user of success.
			commentnotification = True

		#Assumes the comment exists.
		#Add a reply to the comment.
		if 'commentid' in request.POST:
			#Get the publicid of the comment being replied to..
			commentid = request.POST['commentid']
			#Get the comment being replied to by publicid.
			comment_object = Comment.objects.get(publicid=commentid)
			#Get the content of the reply.
			content = request.POST['content']
			#Create a new comment object.
			newcomment = Comment(user=request.user,content=content)
			newcomment.save()
			#Add the comment to the collection of comments.
			comment_object.comments.add(newcomment)
			#Add a variable to notify the user of success.
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
			#Get the form for updating a document, this just replaces 
			#		the file with a new one in the topics collection of documents.
			#	There is no revision control.
		 'update_document_form':form_modal(request,
		 																	#The name of the variable to identify
		 																	#		an update document variable.
																			'updated_documentid',
																			#Get the form html as a table.
																			upload_document_form().as_table(),
																			#This is the title of the bootstrap modal.
																			'Upload a Revised Document',
																			#Create a text/multipart type for the form
																			multipart=True,
																			#Add a special identifier to the form.
																			modal_id="update_document_"+document.publicid,
																			#Add a custom value to the form name, it is
																			#		used to identify the topic.
																			formname_value=document.publicid,
																			#Create a special action for the form to submit to.
																			action=request.get_full_path()
																			),
		 #Create a modal to check if the user wants to delete the 
		 #		document from a collection of topics.
		 'deleted_document_form':form_modal(request,
		 																	#This is the name of the form.
																			'deleted_documentid',
																			#This is the message for the document name.
																			"You will delete '%s'"%document.name,
																			#This is the content of the modal.
																			'Are you sure?',
																			#Add a special identifier to the form.
																			modal_id="deleted_document_"+document.publicid,
																			#Add a custom value to the form name, it is 
																			#			used to identify the topic.
																			formname_value=document.publicid,
																			#Specify a custom request string.
																			action=request.get_full_path(),
																			#Custom submit button text.
																			submit_text="Yes",
																			#A custom button class.
																			submit_button_class="btn-danger",
																			#Custom cancel button text.
																			close_button_text='Cancel',
																			#Custom close button classes.
																			close_button_class='pull-right margin-left-10'
																			),
		 #Get the comments for the topic.
		 'comments':[
		 	#Get the comments for each document.
			{'html':str(recursive_comments(request, comment.publicid))}
			#Run a loop on the comments.
			for comment in document.comments.all()
		],
		#Add a comment to the form.
		'comment_form':comment_form(request,'document',document.publicid),
		}
		#Run a loop on the documents
		for document in topic_object.documents.all()
	]

	#Check to see if the user owns the topic
	if topic_object.user.id == request.user.id:
		#Add a user to the owner of the form.
		user_is_owner = True

	#Load in some context variables.
	context= {
		#The textual title of the page.
		'title':'View Topic',
		#Add a topic to the template.
		'topic': topic,
		#Add documents to the template.
		'documents': documents,
		#A flag for whether or not a success notification
		#		for the comments should go up.
		'commentnotification': commentnotification,
		#A flag for whether or not a success notification
		#		for the release of topic should go up.
		'releasednotification' : releasednotification,
		#A flag for whether or not a success notification
		#		for the updating of a document should go up.
		'updatednotification' : updatednotification,
		#A flag for whether or not an notification for
		#		the updating of a document should go up.
		'deleteddocumentdnotification' : deleteddocumentdnotification,
		#A flag for whether or not a success notification
		#		for the adding of a document to the
		#		collection of topics.
		'addednotification' : addednotification,
		#A flag to indicate if the currently logged  in user
		#		owns the document.
		'user_is_owner' : user_is_owner,
	}

	#Render the template and return it for the user.
	return render(request,
		'topic_management/viewtopic.html',
		context)

###
# Download allows the user to download a file.
#		Any user can download it.
###
@login_required
def download(request,topic_publicid,fileName):
	#Get the filepath for an uploaded document
	filepath = "%s/%s/%s" % (settings.UPLOADED_TOPIC_DIR,topic_publicid,fileName)
  #Open the filepath.
	f = open(filepath,"r")
	#Generate the right mimetype
	mimetype = mimetypes.guess_type(filepath)[0]
	#Assign a default mimetype if none is found.
	if not mimetype: mimetype = "application/octet-stream"
	#Create an HttpResponse with the mimetype
	response = HttpResponse(f.read(),mimetype=mimetype)

	#Microsoft documents error with Content-Disposition
	#		header attached for some reason, however, if you
	#		don't add it doesn't corrupt the file.
	mime_types = (
		'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
		'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	)

	#Check that the mimetype isn't in the mime types above.
	if mimetype not in mime_types:
		#Add a Content-Disposition header to the HttpResponse.
		response["Content-Disposition"] =  "attachment; filename=%s" % os.path.split(filepath)[1]

	#Return the response.
	return response