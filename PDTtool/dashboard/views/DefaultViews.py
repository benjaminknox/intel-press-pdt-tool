
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from dashboard.models import Document
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
"
" The default login url is set in the LOGIN_URL setting.
"
"""

"""
" This is the default view 
"""
########
# ViewDocuments browses through all the documents
#	Up for review.
#	-The view file is viewdocuments.html
########
@login_required
def viewdocuments(request):
	#Check to see if the user has filtered 
	#	the documents.
	if request.method == 'POST':
		#Get the user defined search filter
		search = request.POST['search']
		#Filter the document list based on the users filtered information.
		document_list = Document.objects.filter(name__icontains=search)
	else:
		#Load the document objects into a list
		document_list = Document.objects.all()
	
	#Put the documents into a paginator object
	paginator = Paginator(document_list, 10) # Show 25 documents per page
	#Get the page
	page = request.GET.get('page')

	#This block of code tries loading into a paginator object.
	try:
		#Load the documents for this page.
		documents = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		documents = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		documents = paginator.page(paginator.num_pages)

	#These are view variables.
	context = {
		'title': 'View Documents',
		'documents': documents,
	}	

	#Return the view
	return render(request,
		  		  'dashboard/DefaultViews/viewdocuments.html',
				  context)
"""
" End default views.
"""