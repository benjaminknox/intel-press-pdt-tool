from django.contrib.auth.models import Group, Permission

"""
" Create User Roles (groups in django) based on the use case diagram in the share.
"		-Site Admin.
"		-Supervisor.
"		-Program Manager.
"		-Guest.
"
"I will use this function to access these user roles in the views:
"
"def not_in_student_group(user):
"    if user:
"        return user.groups.filter(name='Student').count() == 0
"    return False
"
"	@user_passes_test(not_in_student_group, login_url='/')
"""
#Try to create groups if the database has been created.
try:
	#Check for the supervisor group.
	Supervisor = Group.objects.filter(name__iexact="Supervisor")
	if not Supervisor:
		#Create the Supervisor group.
		Supervisor = Group(name = "Supervisor")
		Supervisor.save()
		print "Creating Supervisor group."
	else:
		#We have already created the supervisor group.
		print "Supervisor group already created."

	#Check for the ProgramManager group.
	ProgramManager = Group.objects.filter(name__iexact="Program Manager")
	if not ProgramManager:
		#Create the ProgramManager group.
		ProgramManager = Group(name = "Program Manager")
		ProgramManager.save()
		print "Creating Program Manager group."
	else:
		#We have already created the ProgramManager group.
		print "Program Manager group already created."

	#Check for the Guest group.
	Guest = Group.objects.filter(name__iexact="Guest")
	if not Guest:
		#Create the Guest group.
		Guest = Group(name = "Guest")
		Guest.save()
		print "Creating Guest group."
	else:
		#We have already created the Guest group.
		print "Guest group already created."

except:
	print "Issue with group install, try syncing the db."