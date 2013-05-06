from django.http import HttpResponse
from django.core.mail import send_mail
from django.db.models import Q, related
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from dashboard.forms import ExtendeduserForm, MeetingForm
from django.contrib.auth.decorators import login_required
from dashboard.models import Extendeduser,Organization,Meeting,Document

"""
" Supervisor Views
"""
###
# View a list of the users.
###
@login_required
def viewusers(request):

	#Extend the users.
	users = Extendeduser.objects.filter(~Q(user__groups__name='SiteAdministrator'),~Q(user__groups__name='Supervisor'))

	###
	# TODO: Pagination of user objects.
	###

	#Context variables
	context = {
		'title':'Display Users',
		'users' : users,
	}

	#Render the view and return it.
	return render(request,
		  		  'dashboard/Supervisor/viewusers.html',
				  context)

###
# Edit the user.
#	Allows us to update the user.
###
@login_required
def updateuser(request, userid=None):

	if not userid:
		return redirect('/viewusers/')

	#Get the user.
	user_to_update = Extendeduser.objects.get(user__id=userid)

	#Get the groups.
	user_to_update_groups = user_to_update.user.groups.all()

	#Get the active status
	user_to_update_is_active = user_to_update.user.is_active

	#Check if the user is a program manager
	user_to_update_is_program_manager = False
	#Loop through the groups
	for group in user_to_update_groups:
		#Check the name
		if group.name == 'Program Manager':
			#If Program Manager is in the list set
			#	to True.
			user_to_update_is_program_manager = True

	#Manage the post data
	if request.method == 'POST':
	
		#Check for the is_active variable.
		if 'is_active' in request.POST:
			user_to_update.user.is_active = request.POST['is_active']
			user_to_update_is_active = request.POST['is_active']
		else:
			user_to_update.user.is_active = False
			user_to_update_is_active = False

		user_to_update.user.save()

		#Load the program manager group
		program_manager_group = Group.objects.get(name='Program Manager')

		#Check if the user is a program managers
		if 'is_program_manager' in request.POST:
			if not user_to_update_is_program_manager:
				user_to_update.user.groups.add(program_manager_group)
				user_to_update.user.save()
				user_to_update_is_program_manager = True
		else:
			if program_manager_group:
				user_to_update.user.groups.remove(program_manager_group)
				user_to_update_is_program_manager = False

	data = {
		'is_active':user_to_update_is_active,
		'is_program_manager': user_to_update_is_program_manager,
	}

	extendeduserform = ExtendeduserForm(data)

	context = {
		'title':'Update User',
		'user_to_update' : user_to_update,
		'Extendeduserform' : extendeduserform
	}

	#Return the view
	return render(request,
		  		  'dashboard/Supervisor/updateuser.html',
				  context)

def save_meeting_documents(meeting,document_list):

	meeting.documents.clear()

	documents = Document.objects.filter(id__in = document_list)

	for document in documents:

		meeting.documents.add(document)



@login_required
def addmeeting(request):

	if request.method == 'POST':

		meetingform = MeetingForm(request.POST)

		if meetingform.is_valid():
			new_meeting = meetingform.save(commit=False)
			new_meeting.added_user = request.user

			new_meeting.save()

			documents_list = request.POST.getlist('documents')

			save_meeting_documents(new_meeting,documents_list)

			return redirect('/viewmeetings/?added_meeting=%s&start_date=%s' % (new_meeting.name,new_meeting.start_date))

	else:
		meetingform = MeetingForm()

	context ={
		'title': 'Meeting Form',
		'meetingform': meetingform,
		'submit_button_value': 'Add Meeting',
	}

	#Return the view
	return render(request,
		  		  'dashboard/Supervisor/meetingform.html',
				  context)


@login_required
def editmeeting(request,meetingid=None):

	if not meetingid:
		return redirect('/viewmeetings/')

	meeting = Meeting.objects.get(id=meetingid)

	if request.method == 'POST':

		meetingform = MeetingForm(request.POST,instance=meeting)

		if meetingform.is_valid():

			meeting = meetingform.save(commit=False)
			
			meeting.save()

			documents_list = request.POST.getlist('documents')

			save_meeting_documents(meeting,documents_list)

	else:
		meetingform = MeetingForm(instance=meeting)

	context ={

		'title': 'Update %s'% meeting.name,
		'meetingform': meetingform,
		'submit_button_value': 'Update Meeting',

	}

	#Return the view
	return render(request,
		  		  'dashboard/Supervisor/meetingform.html',
				  context)