#from django.forms import ModelForm
from django import forms
from dashboard.models import *
from django.forms import ModelForm,widgets
from django.contrib.auth.models import User

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

"""
" The RegisterForm is a form for registering users.
"	
"	-Views: 'UserAuth.register'
"	-It is loaded into the Authentication library
"		using create_user().
"
"""
class RegisterForm(forms.Form):

	#This runs custom validation
	def clean(self):
		#Clean the userdata that was submit from the form
		cleaned_data = super(RegisterForm, self).clean()

		#Get the cleaned password information
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')

		#Check that the password and confirmed password match
		if password and confirm_password and password != confirm_password:
			#If they don't throw an error on the form
			msg = u"The passwords you entered don't match."
			self._errors['password'] = self.error_class([msg])
			#Delete the confirm password
			del cleaned_data['confirm_password']

		#Find out if the username exists
		username = self.cleaned_data.get('username')
		try:
			#Try querying the username
			user_exists = User.objects.get(username=username)
		
			#If the user exists send an error message
			msg = u"The username you selected already exists."
			self._errors['username'] = self.error_class([msg])
			#Delete the username from the form data
			del cleaned_data['username']
		
		except User.DoesNotExist:
			#Return false if it doesn't
			user_exists = False

		#Return the cleaned_data
		return cleaned_data
	
	#Text input field for the first name.
	first_name = forms.CharField( max_length=255 )

	#Text input field for the last name.
	last_name = forms.CharField( max_length=255 )	

	#Text input field for the username.
	username = forms.CharField( max_length=255 )

	#Password input field for the password.
	password = forms.CharField( max_length=255, widget=forms.PasswordInput)

	#Check Password field.
	confirm_password = forms.CharField( max_length=255, widget=forms.PasswordInput,)

	#An email field for the username.
	email = forms.EmailField( max_length=255 )

class ExtendeduserForm(forms.Form):

	is_active = forms.BooleanField(required=False,label = 'Active')

	#organization = forms.ModelMultipleChoiceField(required=False, queryset = Organization.objects.all(),label="orginization")


class DocumentForm(ModelForm):
	class Meta:
		model = Document

class MeetingForm(ModelForm):
	class Meta:
		model = Meeting

class NotificationForm(ModelForm):
	class Meta:
		model = Notification

class OrganizationForm(ModelForm):
	class Meta:
		model = Organization

class CommentForm(ModelForm):
	class Meta:
		model = Comment