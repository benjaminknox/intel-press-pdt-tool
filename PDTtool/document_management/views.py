from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as userlogin,logout as userlogout
from django.contrib.auth.decorators import login_required

"""
" This is the default view 
"""
########
# ViewDocuments browses through all the documents
#	Up for review.
#	-The view file is viewdocuments.html
########
@login_required(login_url='/documents/login/')
def viewdocuments(request):

	#Load the object resources
	context = {
		'title': 'View Documents',
		}

	#Return the view
	return render(request,
				  'document_management/viewdocuments.html',
				  context)
"""
" End default views.
"""

"""
" The UserAuth Views.
"	TODO: Tie in the UserAuth library, doing custom UserAuth.
"""
########
# Login shows a login screen.
#	-The view file is login.html
########
def login(request):

	if request.user.is_authenticated():
		return redirect('/documents/')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:

				userlogin(request,user)

				if 'next' in request.GET:
					return redirect(request.GET['next'])
				else:
					return redirect('/documents/')

	#Load the object resources
	context = {
		'title': 'User Login',
	}

	#Return the view
	return render(request,
				  'document_management/login.html',
				  context)
########
# Logout logs the user out then shows a logout screen.
########
def logout(request):

	if request.user.is_authenticated():
		userlogout(request)

	return redirect('/documents/login/')


########
# Register shows a user registration screen.
#	-The view file is register.html
########
def register(request):

	if request.user.is_authenticated():
		return redirect('/documents/')

	#Load the object resources
	context = {
		'title': 'User Registration',
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

	if request.user.is_authenticated():
		return redirect('/documents/')
		

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

	if request.user.is_authenticated():
		return redirect('/documents/')

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


"""
" The Admin Management Views.
"""
########
# adduser is a form that allows admins to add users.
#	-The view file is adduser.html
########
@login_required(login_url='/documents/login/')
def adduser(request):

	#Load the object resources
	context = {
		'title': 'Add a user',
	}

	#Return the view
	return render(request,
				  'document_management/adduser.html',
				  context)

########
# updateuser is a form that allows admins to update users.
#	-The view file is updateuser.html
########
@login_required(login_url='/documents/login/')
def updateuser(request, userid = None):

	#Load the object resources
	context = {
		'title': 'Update a User',
	}

	#Return the view
	return render(request,
				  'document_management/updateuser.html',
				  context)


########
# deleteuser is a form that allows admins to delete users.
#	-The view file is deleteuser.html
########
@login_required(login_url='/documents/login/')
def deleteuser(request, userid=None):

	#Load the object resources
	context = {
		'title': 'Delete a User',
	}

	#Return the view
	return render(request,
				  'document_management/deleteuser.html',
				  context)

########
# changeuserpwd is a form that allows admins to change user passwords.
#	-The view file is changeuserpwd.html
########
@login_required(login_url='/documents/login/')
def changeuserpwd(request,userid=None):

	#Load the object resources
	context = {
		'title': 'Change a User Password',
	}

	#Return the view
	return render(request,
				  'document_management/changeuserpwd.html',
				  context)

"""
" End Admin Management Views.
"""

"""
" The Document Management General User Views.
"""
########
# viewdoc is a screen that allows users to view comments,
#		download documents, and later on approve docs.
#	-The view file is viewdoc.html
########
@login_required(login_url='/documents/login/')
def viewdoc(request,documentid=None):

	#Load the object resources
	context = {
		'title': 'View a Document',
	}

	#Return the view
	return render(request,
				  'document_management/viewdoc.html',
				  context)
"""
" End Document Management General User Views.
"""

"""
" The Document Management Author Views.
"		
"		TODO: Getting the file security knowledge.
"""
########
# adddocument is a form that allows an Author to add
#		a document.
#	-The view file is adddocument.html
########
@login_required(login_url='/documents/login/')
def adddocument(request):

	#Load the object resources
	context = {
		'title': 'Add a Document',
	}

	#Return the view
	return render(request,
				  'document_management/adddocument.html',
				  context)

########
# updatedocument is a form that allows an Author to update
#		a document.
#	-The view file is updatedocument.html
########
@login_required(login_url='/documents/login/')
def updatedocument(request, documentid=None):

	#Load the object resources
	context = {
		'title': 'Update a Document',
	}

	#Return the view
	return render(request,
				  'document_management/updatedocument.html',
				  context)

"""
" The Document Management Author Views.
"""