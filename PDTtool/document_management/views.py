from django.shortcuts import render
from django.http import HttpResponse

"""
" This is the default view 
"""
########
# ViewDocuments browses through all the documents
#	Up for review.
#	-The view file is viewdocuments.html
########
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

	#Load the object resources
	context = {
		'title': 'User Login',
	}

	#Return the view
	return render(request,
				  'document_management/login.html',
				  context)

########
# Register shows a user registration screen.
#	-The view file is register.html
########
def register(request):

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