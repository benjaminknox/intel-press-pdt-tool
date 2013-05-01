from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from dashboard.models import Extendeduser,Organization
from dashboard.forms import ExtendeduserForm
from django.db.models import Q, related
from django.contrib.auth.decorators import login_required

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

	user_to_update = Extendeduser.objects.get(user__id=userid)


	if request.method == 'POST':

		"""if 'organization' in request.POST:
			organizations_value = request.POST['organization']

		else:
			organizations_value = []

		organizations = Organization.objects.filter(id__in=)

		for org in organizations:

			if str(org.id) in organizations_value:

				print org.id

				org.users.add(user_to_update.user)
				#org.save()

		"""

		if 'is_active' in request.POST:
			is_active = request.POST['is_active']

		else:
			is_active = False
			
		user_to_update.user.is_active = is_active
		user_to_update.user.save()

	#else:

		#organizations = Organization.objects.filter(users__in=userid)



	#organizations_value = [organization.id for organization in organizations]

	data = {
		'is_active':user_to_update.user.is_active,
		#'organization':organizations_value,
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