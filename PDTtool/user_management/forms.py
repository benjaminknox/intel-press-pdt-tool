#from django.forms import ModelForm
from django import forms
from django.forms import TextInput
from user_management.resources import check_existing_user

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

		#Get the username input
		username = self.cleaned_data.get('username')

		#Check if the user exists.
		if check_existing_user(username):
			#If the user exists send an error message
			msg = u"The username you selected already exists."
			self._errors['username'] = self.error_class([msg])
			#Delete the username from the form data
			del cleaned_data['username']

		#Return the cleaned_data
		return cleaned_data

	#Text input field for the first name.
	first_name = forms.CharField( max_length=255, label='First Name' )

	#Text input field for the last name.
	last_name = forms.CharField( max_length=255, label='Last Name' )

	#Text input field for the username.
	username = forms.CharField( max_length=255 )

	#Text input field for the users phone number.
	phonenumber = forms.CharField( max_length=255, widget=TextInput(attrs={'class':'phone'}), label='Phone Number')

	#Password input field for the password.
	password = forms.CharField( max_length=255, widget=forms.PasswordInput)

	#Check Password field.
	confirm_password = forms.CharField( max_length=255, label='Confirm Password',widget=forms.PasswordInput)

	#An email field for the username.
	email = forms.EmailField( max_length=255 )

"""
" The ForgotPassword form is below
"""
class ForgotPassword(forms.Form):

	#This runs custom validation
	def clean(self):
		#Clean the userdata that was submit from the form
		cleaned_data = super(ForgotPassword, self).clean()
		#Get the username input
		username = self.cleaned_data.get('username')
		#Check if the user exists.
		if not check_existing_user(username):
			#If the user exists send an error message
			msg = u"Couldn't find the username you entered."
			self._errors['username'] = self.error_class([msg])
			#Delete the username from the form data
			del cleaned_data['username']
		#Return the cleaned_data
		return cleaned_data

	#Username of the user
	username = forms.CharField( max_length=255 )

"""
" This is the account settings form.
"""
class AccountSettingsForm(forms.Form):
	#The First Name
	first_name = forms.CharField( max_length=255, label='First Name' )
	#The Last Name
	last_name = forms.CharField( max_length=255, label='Last Name'  )
	#Email
	email = forms.EmailField()
	#Text input field for the users phone number.
	phonenumber = forms.CharField( max_length=255, widget=TextInput(attrs={'class':'phone'}), label='Phone Number')
	#Password
	password = forms.CharField( max_length=255, label="Current Password", widget=forms.PasswordInput,required=False)

"""
" This is for resetting the password.
"""
class ResetPasswordForm(forms.Form):
	#New Password
	newpassword = forms.CharField( max_length=255, label="New Password", widget=forms.PasswordInput(attrs={'autofocus':'autofocus'}),required=False)
	#Confirm Password
	confirmpassword = forms.CharField( max_length=255, label="Confirm Password", widget=forms.PasswordInput,required=False)
	#Current Password
	password = forms.CharField( max_length=255, label="Current Password", widget=forms.PasswordInput,required=False)

class UserManagementForm(AccountSettingsForm):
	#The Username
	username = forms.CharField( max_length=255)
	#The password
	password = forms.CharField( max_length=255, label="Password",required=False)
	#is_active
	is_active = forms.BooleanField(required=False,label="Activated")
	#is_active
	is_program_manager = forms.BooleanField(required=False,label="Program Manager")