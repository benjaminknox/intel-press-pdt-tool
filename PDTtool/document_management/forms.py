#from django.forms import ModelForm
from django import forms
from document_management.models import Document

"""
" The DocumentForm class is a form for
"	uploading to the Document class.
"
"	-Views: 'adddocument'
"
"""
class DocumentForm(forms.Form):

	#The name of the document
	name = forms.CharField( max_length=255 )

    #A short description of the document
    #	written by the uploader
	description = forms.CharField( widget=forms.Textarea )

	#The form.
	#uploadedFiles = MultiuploaderField(required=False)
	file = forms.FileField()

"""
" The RegisterForm is a form for registering users.
"	
"	-Views: 'register', 'adduser'
"	-It is loaded into the Authentication library
"		using create_user().
"
"""
class RegisterForm(forms.Form):

	#Text input field for the first name.
	first_name = forms.CharField( max_length=255 )

	#Text input field for the last name.
	last_name = forms.CharField( max_length=255 )	

	#Text input field for the username.
	username = forms.CharField( max_length=255 )

	#Password input field for the password.
	password = forms.CharField( max_length=255, widget=forms.PasswordInput)

	#Check Password field.
	check_password = forms.CharField( max_length=255, widget=forms.PasswordInput)

	#An email field for the username.
	email = forms.EmailField( max_length=255 )

