from django.shortcuts import render
from document_management.forms import DocumentForm
from document_management.models import Document, File
from django.contrib.auth.decorators import login_required
from document_management.resources import handle_uploaded_file

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
@login_required
def adddocument(request):

	#Load the object resources
	context = {
		'title': 'Add a Document',
		'DocumentForm': DocumentForm(),
	}

	#Check if a file has been posted
	if request.method == 'POST':

		#Get the file
		thefile = request.FILES['file']

		#Get the document post data
		docName = request.POST['name']
		docDesc = request.POST['description']
		docUser = request.user
		#Create a new Document and save it.
		doc = Document(name=docName, description=docDesc,user=docUser)
		doc.save()

		#Single file upload
		#Get the file
		location = '/home/programmer/upload_dir/'+file.name
		fileName = thefile.name
		fileSize = thefile.size
		#Load the document
		document = doc
		#Load a new uploaded file and save it.
		uploadedfile = File(location = location,
						    filename=fileName,
						    size=fileSize,
						    documentid=doc)
		uploadedfile.save()

		#Save the file on to the directory.
		handle_uploaded_file(thefile,location)

		#Add file to the context
		context['file'] = thefile

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