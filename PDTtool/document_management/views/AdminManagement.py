from django.shortcuts import render
from django.contrib.auth.decorators import login_required

"""
" The Admin Management Views.
"""
########
# adduser is a form that allows admins to add users.
#	-The view file is adduser.html
########
@login_required
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
@login_required
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
@login_required
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
@login_required
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
