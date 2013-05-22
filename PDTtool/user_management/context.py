#This lists the groups the user has been assigned.
#	It is loaded in the TEMPLATE_CONTEXT_PROCESSOR
#	variable.
def groups_context(request):

	#Load the users groups.
	usersgroups = {}

	#Create a dictionary with the users groups.
	if request.user:

		#Get the users groups.
		groups = request.user.groups.all()

		#Loop through the groups and add them to the context.
		for g in groups:
			usersgroups[g.name.replace(' ','_')] = True 

		#Load the users groups if they are logged in.
		usersgroups['usersgroups'] = [g.name for g in groups]
	else:
		#If the user is not logged in we add this list.
		usersgroups['usersgroups'] = ['Not Logged In',]

	#Return the dictionary.
	return usersgroups