from django.http import HttpResponse
from django.shortcuts import render, redirect
from dashboard.forms import AddDocumentForm


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
		'AddDocumentForm': AddDocumentForm(),
	}

	#Check if a file has been posted
	if request.method == 'POST':

		#Get the document post data
		docName = request.POST['name']
		docDesc = request.POST['description']
		docUser = request.user
		#Create a new Document and save it.
		doc = Document(name=docName, description=docDesc,user=docUser)
		doc.save()

		#Get the files
		files = request.FILES

		for name,f in files.iteritems():

			#Single file upload
			#Get the file
			fileName = f.name
			location = '/home/programmer/upload_dir/'+f.name
			fileSize = f.size

			#Load a new uploaded file and save it.
			uploadedfile = File(location = location,
							    filename=fileName,
							    size=fileSize,
							    documentid=doc)
			uploadedfile.save()

			#Save the file on to the directory.
			handle_uploaded_file(f,location)

			doc.file.add(uploadedfile)			

		#Return the view
		return render(request,
					  'dashboard/SupervisorProgramManager/adddocumentaction.html',
					  context)

	#Return the view
	return render(request,
				  'dashboard/SupervisorProgramManager/adddocument.html',
				  context)
