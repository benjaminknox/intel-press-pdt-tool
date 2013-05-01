from django.conf.urls import patterns, url
from dashboard.views import DefaultViews, UserAuth, Supervisor

print DefaultViews.viewdocuments

"""
"
" Based on the user roles created in __init__.py:
"	-General User.
"	-Supervisor.
"	-Site Administrator.
"	-Program Manager.
"	-Writer.
"
" Default Route:
"	viewdocuments/ 
"
" UserAuth Routes:
"	login/
"	logout/
"	register/
"
" General User Routes:
"   viewdocument/(:documentid)/
"	viewmeetings/
"	viewmeeting/(:meetingid)/
"	TODO: Get the download header.
"	downloads/(:filename)/
"	usersettings/
"	notifications/
"
" Supervisor and Program Manager:
"	adddocumenttomeeting/(:meetingid)/
"   adddocument/(:documentid)/
"   editdocument/(:documentid)/
"
" Supervisor Routes:
"	-TODO: Email notifications.
"	addmeeting/(:meetingid)/
"	editmeeting/(:meetingid)/
"	deletemeeting/(:meetingid)/
"   viewusers/
"   edituser/(:userid)/
"
" Site Administrator Routes:
"	-TODO: Add a CRUD for each DB object, this is scaffolding.
"   addobject/(:objectname)/
"   objects/(:objectname)/
"   object/(:objectname)/(:objectid)/
"
" Writer's don't have any special routes right now.
"
"""

urlpatterns = patterns('',
	###
	# The default routes, index, and viewdocuments.
	###
    #Here we have our default view which is viewdocuments.
    url(r'^$', DefaultViews.viewdocuments, name='viewdocuments'),
    url(r'^index/', DefaultViews.viewdocuments, name='viewdocuments'),
    url(r'^viewdocuments/', DefaultViews.viewdocuments, name='viewdocuments'),

   	###
	# The UserAuth routes.
	#	login/
	#	logout/
	#	register/
	###
    #Our login view should use the built in Authentication Library.
    url(r'^login/', UserAuth.login, name='login'),
    url(r'^logout/', UserAuth.logout, name='logout'),
    url(r'^register/', UserAuth.register, name='register'),

    #Site Admin Routes
    #url(r'^addobject(?:/(.+))?/$', Supervisor.addobject, name='addobject'),
    #url(r'^objects(?:/(.+))?/$', Supervisor.objects, name='objects'),
    #url(r'^object(?:/(.+)/(\d+))?/$', Supervisor.object, name='object'),

    ###
    # Supervisor Routes:
    #   addmeeting/(:meetingid)/
    #   editmeeting/(:meetingid)/
    #   deletemeeting/(:meetingid)/
    #   viewusers/
    #   edituser/(:userid)/
    ###
    url(r'^viewusers/', Supervisor.viewusers, name='viewusers'),
    url(r'^edituser(?:/(\d+))?/$', Supervisor.edituser, name='edituser'),

)