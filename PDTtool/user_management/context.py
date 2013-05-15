#This lists the groups the user has been assigned.
#	It is loaded in the TEMPLATE_CONTEXT_PROCESSOR
#	variable.
def groups_context(request):

	#Load the users groups.
	usersgroups = {}

	#Create a dictionary with the users groups.
	if request.user:
		#Load the users groups if they are logged in.
		usersgroups['usersgroups'] = [user.name for user in request.user.groups.all()]
	else:
		#If the user is not logged in we add this list.
		usersgroups['usersgroups'] = ['Not Logged In',]

	#Return the dictionary.
	return usersgroups