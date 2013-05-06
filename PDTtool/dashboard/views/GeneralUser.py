from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Document, File, Comment, Meeting
from dashboard.resources import comment_form, recursive_comments, MeetingCalendar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
"
" The default login url is set in the LOGIN_URL setting.
"
"""

"""
" The Document Management General User Views.
"""
########
# viewdoc is a screen that allows users to view comments,
#		download documents, and later on approve docs.
#	-The view file is viewdoc.html
########
@login_required
def viewdocument(request,documentid=None):

	##TODO: recode this page.

	#Check to see if the documentid is set
	if documentid:

		#Get the document.
		document = Document.objects.get(id=documentid)

		#If the document is deleted redirect.
		if document.deleted:

			return redirect('/')
		
		#If a document has been deleted.
		if request.method == 'POST' and 'deleted_documentid' in request.POST:
			#Document is deleted
			document.deleted = True
			document.save()

			#Return the redirect.
			return redirect('/')

		#If a comment has been posted.
		if request.method == 'POST' and 'content' in request.POST:
			#Get the post data
			content = request.POST['content']
			title = request.POST['title']

			#Create a new comment.
			newcomment = Comment(user=request.user,content=content,title=title,reported=False)
			newcomment.save()

			if 'commentid' in request.POST:

				print "Comment"

				commentid = request.POST['commentid']
				comment = Comment.objects.get(id=commentid)
				comment.comments.add(newcomment)
			
			elif 'fileid' in request.POST:

				print "File"

				fileid = request.POST['fileid']
				file_object = File.objects.get(id=fileid)
				file_object.comments.add(newcomment)

			#It is a comment on a document.
			else:

				print "Document"

				#Add the comment to the document
				document.comments.add(newcomment)

		#Get all of the files associated with the document.
		files = File.objects.filter(documentid=documentid)

		#Get all fo the comments associated with the document.
		comments = document.comments.all()

		list_of_comments = ""

		for comment in comments:
			list_of_comments += recursive_comments(request,comment.id)

		files_with_comments = []

		for f in files:

			file_comments = ""

			for fcomment in f.comments.all():
				file_comments += recursive_comments(request,fcomment.id)

			files_with_comments.append({

				'queryset': f,
				'comments': file_comments,
				'file_comment_form': comment_form(request,'file',f.id)

			})

		#Load the object resources
		context = {
			'title': 'View a Document',
			'document': document,
			'files' : files_with_comments,
			'list_of_comments' : list_of_comments,
			'documentid' : documentid,
			'document_comment_form': comment_form(request,'document',documentid)
		}

		#Return the view
		return render(request,
					  'dashboard/GeneralUser/viewdocument.html',
					  context)

	#Redirect to the home page.
	return redirect('/')

@login_required
def viewmeetings(request):

	#If a document has been deleted.
	if request.method == 'POST' and 'deleted_meetingid' in request.POST:

		deleted_meetingid = request.POST['deleted_meetingid']
		meeting = Meeting.objects.get(id=deleted_meetingid)
		#Meeting is deleted
		meeting.deleted = True
		meeting.save()

	#Check to see if the user has filtered 
	#	the meetings.
	if request.method == 'POST' and False == True:
		#Get the user defined search filter
		search = request.POST['search']
		#Filter the meeting list based on the users filtered information.
		meeting_list = Meeting.objects.filter(name__icontains=search,deleted=False)
	else:
		#Load the meeting objects into a list
		meeting_list = Meeting.objects.filter(deleted=False)
	
	#Put the meetings into a paginator object
	paginator = Paginator(meeting_list, 10) # Show 25 meetings per page
	#Get the page
	page = request.GET.get('page')

	#This block of code tries loading into a paginator object.
	try:
		#Load the meetings for this page.
		meetings = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		meetings = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		meetings = paginator.page(paginator.num_pages)

	year = 2013
	month = 05

	cal = MeetingCalendar(meetings).formatmonth(year, month)

	#These are view variables.
	context = {
		'title': 'View Meetings',
		#Load in the documents paginator
		'meetings': meetings,
		'calendar': cal,
	}	
	#Return the view
	return render(request,
		  		  'dashboard/GeneralUser/viewmeetings.html',
				  context)
"""
" End Document Management General User Views.
"""