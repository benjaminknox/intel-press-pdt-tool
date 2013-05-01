from django.http import HttpResponse
from django.shortcuts import render, redirect

def adddocument(request):

	context = {
		'title': 'Add Document',
	}

	#Render the view and return it.
	return render(request,
		  		  'dashboard/SupervisorProgramManager/adddocument.html',
				  context)