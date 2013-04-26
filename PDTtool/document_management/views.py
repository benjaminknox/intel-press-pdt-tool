import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from document_management.models import Document, File, Comment
from document_management.forms import DocumentForm,RegisterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login as userlogin,logout as userlogout

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
		  		  'document_management/viewdocuments.html',
				  context)
"""
" End default views.
"""

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

"""
" The Document Management General User Views.
"""
########
# viewdoc is a screen that allows users to view comments,
#		download documents, and later on approve docs.
#	-The view file is viewdoc.html
########
@login_required
def viewdoc(request,documentid=None):

	if documentid :DOc

		document = Document.objects.get(id=documentid)

		if request.method == 'POST':
			content = request.POST['content']
			title = request.POST['title']
			newcomment = Comment(user=request.user,content=content,title=title,reported=False)
			newcomment.save()

			document.comments.add(newcomment)

		files = File.objects.filter(documentid=documentid)

		comments = document.comments.all()

		#Load the object resources
		context = {
			'title': 'View a Document',
			'document': document,
			'files' : files,
			'comments' : comments,
		}

		#Return the view
		return render(request,
					  'document_management/viewdoc.html',
					  context)

	return redirect('/')
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

def handle_uploaded_file(f,location):
    with open(location, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return location

def save_uploaded_file(request):
	return HttpResponse("Uploaded file.")

@login_required
def adddocument(request):

	#Load the object resources
	context = {
		'title': 'Add a Document',
		'DocumentForm': DocumentForm(),
	}

	if request.method == 'POST':

		#Get the file
		file = request.FILES['file']

		#Get the document
		docName = request.POST['name']
		docDesc = request.POST['description']
		docUser = request.user
		doc = Document(name=docName, description=docDesc,user=docUser)
		doc.save()

		#Single file upload
		#Get the file
		location = '/home/programmer/upload_dir/'+file.name
		fileName = file.name
		fileSize = file.size
		document = doc
		uploadedfile = File(location = location,
						    filename=fileName,
						    size=fileSize,
						    documentid=doc)
		uploadedfile.save()

		#Save the file
		handle_uploaded_file(file,location)

		context['file'] = file

		#Return the view
		return render(request,
					  'document_management/adddocumentaction.html',
					  context)

	#Return the view
	return render(request,
				  'document_management/adddocumentform.html',
				  context)

########
# updatedocument is a form that allows an Author to update
#		a document.
#	-The view file is updatedocument.html
########
@login_required
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