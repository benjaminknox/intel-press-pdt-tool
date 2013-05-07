from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login(request):

	context = {
		'title':'PDT Portal - Login'
	}

	return render(request,
		  		  'user_management/login.html',
				  context)