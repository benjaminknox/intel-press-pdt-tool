from django.contrib.auth.models import Group, Permission

"""
" Create User Roles (groups in django) based on the use case diagram in the share.
"		-General User.
"		-Supervisor.
"		-Program Manager.
"		-Writer.
"
" I will use this function to access these user roles in the views:
"
"def not_in_student_group(user):
"    if user:
"        return user.groups.filter(name='Student').count() == 0
"    return False
"
"	@user_passes_test(not_in_student_group, login_url='/')
"""

try:
	GeneralUser = Group.objects.filter(name__iexact="General User")
	if not GeneralUser:
		GeneralUser = Group(name = "General User")
		GeneralUser.save()
		print "Creating General User group."
	else:
		print "General User group already created."

	Supervisor = Group.objects.filter(name__iexact="Supervisor")
	if not Supervisor:
		#Create the Supervisor group.
		Supervisor = Group(name = "Supervisor")
		Supervisor.save()
		#Create the Supervisor permissions
		print "Creating Supervisor group."
	else:
		print "Supervisor group already created."

	ProgramManager = Group.objects.filter(name__iexact="Program Manager")
	if not ProgramManager:
		ProgramManager = Group(name = "Program Manager")
		ProgramManager.save()
		print "Creating Program Manager group."
	else:
		print "Program Manager group already created."

	Writer = Group.objects.filter(name__iexact="Writer")
	if not Writer:
		Writer = Group(name = "Writer")
		Writer.save()
		print "Creating Writer group."
	else:
		print "Writer group already created."
except:
	print "Issue with group install, try syncing the db."