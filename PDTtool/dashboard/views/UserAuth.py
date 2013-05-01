from django.http import HttpResponse
from dashboard.forms import RegisterForm
from dashboard.models import Extendeduser
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from dashboard.resources import user_is_authenticated_decorator
from django.contrib.auth import authenticate,login as userlogin,logout as userlogout

"""
" The UserAuth Views.
"""
########
# Login shows a login screen.
#	-The view file is login.html
########
@user_is_authenticated_decorator
def login(request):

	#Load the view variables.
	context = {
		'title': 'User Login',
		'loginerror': False
	}
	"""
	" This is the login logic.
	"""
	if request.method == 'POST' and request.POST['username'] is not None and request.POST['password'] is not None:

		#Get the formdata
		formdata = {
			#Get the user input
			'username' : request.POST['username'],
			'password' : request.POST['password'],
		}

		#Authenticate the user based on their input.
		user = authenticate(username=formdata['username'], password=formdata['password'])
		
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
		else:
			context['loginerror'] = True

	"""
	" End the login logic.
	"""

	"""
	" Load the login form.
	"	This is run if:
	"	-User is not authenticated.
	"	-No POST information.
	"""
	context['AuthenticationForm'] = AuthenticationForm

	#Return the view
	return render(request,
				  'dashboard/UserAuth/login.html',
				  context)
	"""
	" End login form loading
	"""

########
# Logout logs the user out then shows a logout screen.
########
@login_required
def logout(request):
	if request.user.is_authenticated():
		userlogout(request)

	return redirect('/login/')

########
# Register shows a user registration screen.
#	-The view file is register.html
########
@user_is_authenticated_decorator
def register(request):
	
	#Load the context variables
	context = {
		'title': 'User Registration',
	}

	#Check the post request.
	if request.method == 'POST':

		#Get the formdata 
		formdata = {
			'first_name' : request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'username' : request.POST['username'],
			#Password and confirm password are validated against each other.
			'password' : request.POST['password'],
			'confirm_password' : request.POST['confirm_password'],
			'email' : request.POST['email']
		}

		###
		# We bind the post data to the form here for validation.
		###
		registerform = RegisterForm(formdata)

		#Make sure the register form passed the validation
		if registerform.is_valid():

			#Create the user object.
			newuser = User.objects.create_user(first_name=formdata['first_name'],
									 last_name=formdata['last_name'],
									 username=formdata['username'],
									 password=formdata['password'],
									 email=formdata['email'])
			#Initially the user is inactive, activated by super user.
			newuser.is_active = False
			
			#Save the user object.
			newuser.save()

			#Add the general user group to the new user.
			GeneralUserGroup = Group.objects.get(name='General User')
			newuser.groups.add(GeneralUserGroup)

			#Add the Extended user row
			extuser = Extendeduser(user=newuser)
			extuser.save()

			#Return the success view
			return render(request,
						  'dashboard/UserAuth/registersuccess.html',
						  context)
	else:
		###
		# Create an unbound form because
		#	there isn't any post data.
		###
		registerform = RegisterForm()
		
	"""
	" The below code happens if:
	"	-There is no post data.
	"	-The submitted form is invalid.
	"""

	context['RegisterForm'] = registerform

	#Return the view
	return render(request,
				  'dashboard/UserAuth/register.html',
				  context)

########
# forgotpwd shows a form for allowing the user
#	to have their password emailed to them.
#	-The view file is forgotpwd.html
########
@user_is_authenticated_decorator
def forgotpwd(request):

	#Load the object resources
	context = {
		'title': 'Forgotten Password Form',
	}

	#Return the view
	return render(request,
				  'dashboard/UserAuth/forgotpwd.html',
				  context)

########
# forgotusername shows a form for allowing the user
#	to have their username emailed to them.
#	-The view file is forgotusername.html
########
@user_is_authenticated_decorator
def forgotusername(request):

	#Load the object resources
	context = {
		'title': 'Forgotten Username Form',
	}

	#Return the view
	return render(request,
				  'dashboard/UserAuth/forgotusername.html',
				  context)

"""
" End UserAuth views.
"""
