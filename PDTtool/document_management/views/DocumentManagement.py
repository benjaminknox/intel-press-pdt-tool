from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from document_management.models import Document, File, Comment

"""
" The Document Management General User Views.
"""
########
# viewdoc is a screen that allows users to view comments,
#		download documents, and later on approve docs.
#	-The view file is viewdoc.html
########
@login_required
def viewdoc(request,documentid=None):

	#Check to see if the documentid is set
	if documentid:

		#Get the document.
		document = Document.objects.get(id=documentid)

		#If a comment has been posted.
		if request.method == 'POST':
			#Get the post data
			content = request.POST['content']
			title = request.POST['title']

			#Create a new comment.
			newcomment = Comment(user=request.user,content=content,title=title,reported=False)
			newcomment.save()

			#Add the comment to the document
			document.comments.add(newcomment)

		#Get all of the files associated with the document.
		files = File.objects.filter(documentid=documentid)

		#Get all fo the comments associated with the document.
		comments = document.comments.all()

		#Load the object resources
		context = {
			'title': 'View a Document',
			'document': document,
			'files' : files,
			'comments' : comments,
		}

		#Return the view
		return render(request,
					  'document_management/viewdoc.html',
					  context)

	#Redirect to the home page.
	return redirect('/')
"""
" End Document Management General User Views.
"""