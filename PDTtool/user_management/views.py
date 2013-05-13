from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from pdtresources.decorators import user_is_authenticated_decorator
from user_management.forms import RegisterForm, ForgotPassword, AccountSettingsForm
from user_management.models import ExtendedUser, ActivateUserDB
from django.contrib.auth import authenticate,login as userlogin,logout as userlogout
from user_management.resources import send_activation_email, send_password_reset_email, send_new_password_email

########
# Login shows a login screen.
#	-The view file is /user_management/login.html
########
@user_is_authenticated_decorator
def login(request):

	#Load the view variables.
	context = {
		'title': 'User Login',
		'loginerror': False,
		'loginscreen' : True,
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
				context['loginerror'] = "You have not been activated, please check your email"
		else:
			context['loginerror'] = "Incorrect username or password"

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

	return render(request,
		  		  'user_management/login.html',
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
			'phonenumber' : request.POST['phonenumber'],
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
			#GeneralUserGroup = Group.objects.get(name='General User')
			#newuser.groups.add(GeneralUserGroup)

			#Add the Extended user row
			extuser = ExtendedUser(user=newuser,phonenumber=formdata['phonenumber'])
			extuser.save()

			#Send the activation email, contains a publicid.
			send_activation_email(newuser)

			#Return the success view
			return render(request,
						  'user_management/registersuccess.html',
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
				  'user_management/register.html',
				  context)

########
# Activate the user based on the publicid.
#	-The view file is user_management/activate.html 
########
@user_is_authenticated_decorator
def activate(request):
	if request.method == 'GET' and 'publicid' in request.GET and 'userid' in request.GET:

		#Get the publicid_string
		publicid_string = request.GET['publicid']

		#Get the publicid_string
		extendeduser_publicid = request.GET['userid']

		context = {
			'title':'Activate Account',
			'activated' : False,
			'message' : None,
		}

		try:
			#Get the publicid database field
			publicid = ActivateUserDB.objects.get(publicid=publicid_string)
			#Get the publicid database field
			extendeduser = ExtendedUser.objects.get(publicid=extendeduser_publicid)
		except:
			#publicid doesn't exist anymore
			publicid = False
			#Get the publicid database field
			extendeduser = False

		#Check if the publicid exists
		if publicid and extendeduser:

			#Activate the user
			publicid.user.is_active = True
			publicid.user.save()

			#Delete the publicid
			publicid.delete()

			#Turn on the activated context
			context['activated'] = True

			#Assign a message.
			context['message'] = "Your account has been successfully accessed."

		#If the publicid doesn't exist
		else:

			#Turn on the activated context
			context['activated'] = False

			#Assign a message.
			context['message'] = "Sorry the reset password request doesn't exist anymore."

			#Send to the user register page.
			return redirect('/login/')

		return render(request,
				'user_management/activate.html',
				context)
	else:
		#If there is no id redirect to the login screen.
		return redirect('/login/')


########
# A series of forgot password screens.
#	-The view file is user_management/forgotpassword.html 
########
@user_is_authenticated_decorator
def forgotpassword(request):

	context = {
		'title':'Forgot Password',
	}

	if request.method == 'GET' and 'publicid' in request.GET and 'userid' in request.GET:

		#Get the publicid_string
		publicid_string = request.GET['publicid']

		#Get the publicid_string
		extendeduser_publicid = request.GET['userid']

		try:
			#Get the publicid database field
			publicid = ActivateUserDB.objects.get(publicid=publicid_string)
			#Get the publicid database field
			extendeduser = ExtendedUser.objects.get(publicid=extendeduser_publicid)
		except:
			#publicid doesn't exist anymore
			publicid = False
			#The user doesn't exist.
			extendeduser = False

		#Check if the publicid exists
		if publicid and extendeduser:

			#Generate a random password
			newpassword = User.objects.make_random_password(length=8)
			#Reset the user password
			publicid.user.set_password(newpassword)
			publicid.user.save()
			#Delete the publicid
			publicid.delete()

			#Email the password to the user
			send_new_password_email(publicid.user,newpassword)

			return render(request,
				'user_management/forgotpasswordresetlink.html',
				context)

	#Check for post data.
	if request.method == 'POST':
		#If post data exists bind it to the form.
		forgotpassword = ForgotPassword(request.POST)

		#If the form is valid
		if forgotpassword.is_valid():

			#Get the username.
			username = request.POST['username']

			#Get the user
			user = User.objects.get(username=username)
			#Send the reset password email
			send_password_reset_email(user)

			return render(request,
					'user_management/forgotpasswordresetemail.html',
					context)

	else:
		#Create an unbound forgot password form.
		forgotpassword = ForgotPassword()

	#Add the ForgotPassword to the form.		
	context['ForgotPassword'] = forgotpassword

	return render(request,
			'user_management/forgotpassword.html',
			context)

########
# These are the account settings, editing user content.
#	-The view file is user_management/forgotpassword.html 
########
@login_required
def accountsettings(request):

	extendeduser = ExtendedUser.objects.get(user=request.user)

	context = {
		'title':'Account Settings',
	}

	#Check for the POST method
	if request.method == 'POST':

		#Get the account settings form with 
		#		the POST data bound to it.
		accountsettingsform = AccountSettingsForm(request.POST)
	
		#Get the first name field
		first_name = request.POST['first_name']
		#Get the last name field
		last_name = request.POST['last_name']
		#Get the email field
		email = request.POST['email']
		#Get the password field
		password = request.POST['password']
		#Get the phone number field
		phonenumber = request.phonenumber

		#Check the password of the user
		if request.user.check_password(password):
			#Reset the user First Name
			request.user.first_name = first_name
			#Reset the user Last Name
			request.user.last_name = last_name
			#Reset the user email
			request.user.email = email
			#Save the phonenumber
			extendeduser.phonenumber = phonenumber
			#Save the user.
			request.user.save()

	else:
		#If there is no post data
		first_name = request.user.first_name
		last_name = request.user.last_name
		email = request.user.email
		phonenumber = extendeduser.phonenumber

		user_form_contents = {
			'first_name':first_name,
			'last_name':last_name,
			'email':email,
			'phonenumber':phonenumber,
		}

		accountsettingsform = AccountSettingsForm(user_form_contents)

	context['AccountSettingsForm'] = accountsettingsform

	return render(request,
			'user_management/accountsettings.html',
			context)

def resetpassword(request):

	context = {
		'title':'Reset Password',
	}

	return render(request,
			'user_management/resetpassword.html',
			context)