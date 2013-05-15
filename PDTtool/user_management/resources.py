from uuid import uuid4
from django.core.mail import send_mail
from django.contrib.auth.models import User
from user_management.models import ExtendedUser, ActivateUserDB, ForgotPasswordDB

#This is the website domain, no http://.
domain = '127.0.0.1:5486'

# This sends an activation email, with a publicid in it.
#		it requires a User model object, and and uses
#		the ActivateUserDB model. It also uses the
#		uuid.uuid4() method.
def send_activation_email(inactive_user):

	#Get the extended user object
	extendeduser = ExtendedUser.objects.get(user=inactive_user)

	#Get the extendeduser publicid
	extendeduser_publicid = extendeduser.publicid

	#Get the publicid
	publicid_string = uuid4()

	#Create a publicid value.
	publicid = ActivateUserDB(user=inactive_user,publicid=publicid_string)

	#Save the publicid
	publicid.save()

	#Define the from email.
	from_email = 'the.pdt.portal@gmail.com'

	#Get the inactive users email.
	to_email = [inactive_user.email]

	#Get the first name.
	first_name = inactive_user.first_name

	#Get the last name.
	last_name = inactive_user.last_name

	#Get the subject.
	subject = "PDT Portal Account Activation"

	#Define a message.
	message = "Thank you for registering to the PDT Portal %s %s,\r\n\r\n"%(first_name,last_name)
	message+= "To activate your account go to this link: http://%s/activate/?publicid=%s&userid=%s" % (domain, publicid_string,extendeduser_publicid)

	#Send the email.
	send_mail(subject, message, from_email, to_email, fail_silently=False)


# This sends password reset email, with a publicid in it.
#		it requires a User model object, and and uses
#		the ForgotPasswordDB model. It also uses the
#		uuid.uuid4() method.
def send_password_reset_email(user):

	#Get the extended user object
	extendeduser = ExtendedUser.objects.get(user=user)

	#Get the extendeduser publicid
	extendeduser_publicid = extendeduser.publicid

	#Get the publicid
	publicid_string = uuid4()

	#Create a publicid value.
	publicid = ForgotPasswordDB(user=user,publicid=publicid_string)

	#Save the publicid
	publicid.save()

	#Define the from email.
	from_email = 'the.pdt.portal@gmail.com'

	#Get the inactive users email.
	to_email = [user.email]

	#Get the first name.
	first_name = user.first_name

	#Get the last name.
	last_name = user.last_name

	#Get the subject.
	subject = "PDT Portal Reset Password"

	#Define a message.
	message = "Hi %s %s,\r\n\r\n" % (first_name,last_name)
	message+= "To reset your password go to this link: http://%s/forgotpassword/?resetid=%s&userid=%s" % (domain, publicid_string,extendeduser_publicid)

	#Send the email.
	send_mail(subject, message, from_email, to_email, fail_silently=False)


# This sends the new password to the user.
#		it requires a User model object, and and uses
#		the ForgotPasswordDB model. It also uses the
#		uuid.uuid4() method.
def send_new_password_email(user, newpassword):

	#Define the from email.
	from_email = 'the.pdt.portal@gmail.com'

	#Get the inactive users email.
	to_email = [user.email]

	#Get the first name.
	first_name = user.first_name

	#Get the last name.
	last_name = user.last_name

	#Get the subject.
	subject = "PDT Portal New Password"

	#Define a message.
	message = "Hi %s %s,\r\n\r\n" % (first_name,last_name)
	message+= "Your new password is %s, please reset this right away." % newpassword

	#Send the email.
	send_mail(subject, message, from_email, to_email, fail_silently=False)

#This checks to see if a user exists 
#		based on the username.
def check_existing_user(username):
	try:
		#Try querying the username
		user_exists = User.objects.get(username=username)
	except User.DoesNotExist:
		#The username does not exist.
		user_exists = False

	#Return the value of the user
	return user_exists

#Check if a user has a group.
def check_user_groups(user, groupstocheck):
	#Check that it is a string.
	if isinstance(groupstocheck,str):
		#Create a list to iterate over.
		groupstocheck = [groupstocheck,]

	#Create a flag to return.
	user_has_group = False

	#Get the user groups.
	usergroups = user.groups.all()

	#Loop through the groups to check.
	for grouptocheckname in groupstocheck:
		#Loop through the groups that the provided user has.
		for gobj in usergroups:
			#Check the name of the group object with the group.
			if gobj.name == grouptocheckname:
				#If the group is in it flag it.
				user_has_group = True

	#Return the user group.
	return user_has_group
