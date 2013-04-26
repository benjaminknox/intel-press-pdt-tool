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