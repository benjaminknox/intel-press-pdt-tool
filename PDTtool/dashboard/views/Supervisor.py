from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from dashboard.models import Extendeduser
from django.db.models import Q, related
from django.contrib.auth.decorators import login_required

@login_required
def viewusers(request):

	users = Extendeduser.objects.filter(~Q(user__groups__name='SiteAdministrator'),~Q(user__groups__name='Supervisor'))

	context = {
		'title':'Display Users',
		'users' : users,
	}

	#Return the view
	return render(request,
		  		  'dashboard/Supervisor/viewusers.html',
				  context)

@login_required
def edituser(request, userid=None):

	if not userid:
		return redirect('/viewusers/')

	user = Extendeduser.objects.get(user__id=userid)

	context = {
		'title':'Edit User',
		'user_to_edit' : user
	}

	#Return the view
	return render(request,
		  		  'dashboard/Supervisor/edituser.html',
				  context)