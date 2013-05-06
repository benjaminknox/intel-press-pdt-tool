from django.conf.urls import patterns, url
from dashboard.views import DefaultViews, UserAuth, Supervisor, GeneralUser, SupervisorProgramManager

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
"   updateuser/(:userid)/
"
" Site Administrator Routes:
"   -Using the django Admin app.
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

    ###
    # General User Routes:
    #   viewdocument/(:documentid)/
    #   viewmeetings/
    ###
    url(r'^viewdocument(?:/(\d+))?/$', GeneralUser.viewdocument, name='viewdocument'),
    url(r'^viewmeetings/', GeneralUser.viewmeetings, name='viewmeetings'),

    ###
    # Supervisor Routes:
    #   addmeeting/
    #   editmeeting/(:meetingid)/
    #   deletemeeting/(:meetingid)/
    #   viewusers/
    #   updateuser/(:userid)/
    ###
    url(r'^viewusers/', Supervisor.viewusers, name='viewusers'),
    url(r'^updateuser(?:/(\d+))?/$', Supervisor.updateuser, name='updateuser'),
    url(r'^addmeeting/', Supervisor.addmeeting, name='addmeeting'),
    url(r'^editmeeting(?:/(\d+))?/$', Supervisor.editmeeting, name='editmeeting'),

    ###
    # Supervisor and Program Manager:
    #   adddocumenttomeeting/(:meetingid)/
    #   adddocument/(:documentid)/
    #   editdocument/(:documentid)/
    ###
    url(r'^adddocument/$', SupervisorProgramManager.adddocument, name='adddocument'),
)