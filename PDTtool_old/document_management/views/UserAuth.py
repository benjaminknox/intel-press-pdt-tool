from django.http import HttpResponse
from django.shortcuts import render, redirect
from document_management.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as userlogin,logout as userlogout


"""
" The UserAuth Views.
"""
########
# Login shows a login screen.
#	-The view file is login.html
########
def login(request):

	#Check if the user is authenticated.
	if request.user.is_authenticated():
		#redirect to the base url.
		return redirect('/')

	"""
	" This is the login logic.
	"""
	if request.method == 'POST':
		#Get the user input
		username = request.POST['username']
		password = request.POST['password']
		
		#Authenticate the user based on their input.
		user = authenticate(username=username, password=password)
		
		#Check if the user authenticated properly.
		if user is not None:

			#Check if the user is active.
			if user.is_active:

				#Login the user
				userlogin(request,user)

				#Check the next variable in the url
				#	for redirect to the original request.
				if 'next' in request.GET:
					#Redirect to the original request.
					return redirect(request.GET['next'])
				else:
					#Redirect to the default view.
					return redirect('/')
	"""
	" End the login logic.
	"""

	"""
	" Load the login form.
	"	This is run if:
	"	-User is not authenticated.
	"	-No POST information.
	"""
	#Load the view variables.
	context = {
		'title': 'User Login',
		'AuthenticationForm': AuthenticationForm,
	}

	#Return the view
	return render(request,
				  'document_management/login.html',
				  context)
	"""
	" End login form loading
	"""

########
# Logout logs the user out then shows a logout screen.
########
def logout(request):

	if request.user.is_authenticated():
		userlogout(request)

	return redirect('/login/')


########
# Register shows a user registration screen.
#	-The view file is register.html
# 	TODO: register the user.
########
def register(request):

	if request.method == 'POST':

		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password = request.POST['password']
		checkpassword = request.POST['checkpassword']
		email = request.POST['email']

		if password == checkpassword:
			create_user(first_name=first_name,
						last_name=last_name,
						username=username,
						password=password,
						email=email)

	#Check if the user is authenticated.
	if request.user.is_authenticated():
		return redirect('/')

	#Load the object resources
	context = {
		'title': 'User Registration',
		'RegisterForm': RegisterForm,
	}

	#Return the view
	return render(request,
				  'document_management/register.html',
				  context)

########
# forgotpwd shows a form for allowing the user
#	to have their password emailed to them.
#	-The view file is forgotpwd.html
########
def forgotpwd(request):

	#Check if the user is authenticated.
	if request.user.is_authenticated():
		return redirect('/')
	
	#Load the object resources
	context = {
		'title': 'Forgotten Password Form',
	}

	#Return the view
	return render(request,
				  'document_management/forgotpwd.html',
				  context)

########
# forgotusername shows a form for allowing the user
#	to have their username emailed to them.
#	-The view file is forgotusername.html
########
def forgotusername(request):

	#Check if the user is authenticated.
	if request.user.is_authenticated():
		return redirect('/')

	#Load the object resources
	context = {
		'title': 'Forgotten Username Form',
	}

	#Return the view
	return render(request,
				  'document_management/forgotusername.html',
				  context)

"""
" End UserAuth views.
"""
