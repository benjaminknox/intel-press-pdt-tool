from django.http import HttpResponse
from django.shortcuts import render, redirect
from dashboard.forms import AddDocumentForm

def adddocument(request):

	context = {
		'title': 'Add Document',
		'AddDocumentForm': AddDocumentForm,
	}

	#Render the view and return it.
	return render(request,
		  		  'dashboard/SupervisorProgramManager/adddocument.html',
				  context)