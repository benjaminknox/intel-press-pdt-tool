from django.http import HttpResponse
from django.shortcuts import render, redirect
from dashboard.models import *
from dashboard.forms import DocumentForm, MeetingForm, NotificationForm, OrganizationForm, CommentForm

#In development, this is the scaffolding.

def addobject(request,objectname=None):
	
	context = {
		'title':'Add %s Object' % objectname,
	}

	#Scoffolding Pick up on it later.
	#if request.method == 'POST':

	form = eval('%sForm' % objectname)

	context['form'] = form

	#Return the view
	return render(request,
		  		  'dashboard/SiteAdministrator/addobject.html',
				  context)

def objects(request,objectname=None):
	
	context = {
		'title':'List %s Objects' % objectname,
		'objectname' : objectname,
	}

	objects = eval('%s.objects.all()' % objectname)

	context['objects'] = objects

	#Return the view
	return render(request,
		  		  'dashboard/SiteAdministrator/objects.html',
				  context)

def object(request,objectname=None,objectid=None):
	
	context = {
		'title':'%s Object | # %s' % (objectname, objectid),
	}

	#Return the view
	return render(request,
		  		  'dashboard/SiteAdministrator/object.html',
				  context)