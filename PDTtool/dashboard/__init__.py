from django.contrib.auth.models import Group, Permission

"""
" Create User Roles (groups in django).
"""

Supervisor = Group.objects.filter(name__iexact="Supervisor")
if not Supervisor:
	#Create the Supervisor group.
	Supervisor = Group(name = "Supervisor")
	Supervisor.save()
	#Create the Supervisor permissions
	print "Creating Supervisor group. \n"
else:
	print "Supervisor group already created. \n"

SiteAdministrator = Group.objects.filter(name__iexact="Site Administrator")
if not SiteAdministrator:
	SiteAdministrator = Group(name = "Site Administrator")
	SiteAdministrator.save()
	print "Creating Site Administrator group. \n"
else:
	print "Site Administrator group already created. \n"

ProgramManager = Group.objects.filter(name__iexact="Program Manager")
if not ProgramManager:
	ProgramManager = Group(name = "Program Manager")
	ProgramManager.save()
	print "Creating Program Manager group. \n"
else:
	print "Program Manager group already created. \n"

Writer = Group.objects.filter(name__iexact="Writer")
if not Writer:
	Writer = Group(name = "Writer")
	Writer.save()
	print "Creating Writer group. \n"
else:
	print "Writer group already created. \n"

GeneralUser = Group.objects.filter(name__iexact="General User")
if not GeneralUser:
	GeneralUser = Group(name = "General User")
	GeneralUser.save()
	print "Creating General User group. \n"
else:
	print "General User group already created. \n"