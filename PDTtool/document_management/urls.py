from django.conf.urls import patterns, url
from document_management.views import DefaultViews, UserAuth, AdminManagement, DocumentManagement, DocumentManagementAuthor

"""
" Url Schema:
"
"	-The standard index routes to the view 'viewdocuments'.
"	-The default view is 'viewdocuments'.
"
"Default Route:
"	viewdocuments/  <-browse
"
"UserAuth Scheme:
"	login/
"	logout/
"	register/
"	forgotpwd/
"	forgotusername/
"
"Admin Management Scheme:
"	adduser/
"	updateuser/(:userid)/
"	deleteuser/(:userid)/
"	changeuserpwd/(:userid)/
"
"Document Management General User Scheme:
"	viewdoc/(:documentid)/
"
"Document Management Author Scheme:
"	adddocument/
"	updatedocument/(:documentid)/
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
	# End default routes
	###

	###
	# The UserAuth routes.
	#	login/
	#	register/
	#	forgotpwd/
	#	forgotusername/
	###
    #Our login view should use the built in Authentication Library.
    url(r'^login/', UserAuth.login, name='login'),
    url(r'^logout/', UserAuth.logout, name='logout'),
    url(r'^register/', UserAuth.register, name='register'),
    url(r'^forgotpwd/', UserAuth.forgotpwd, name='forgotpwd'),
    url(r'^forgotusername/', UserAuth.forgotusername, name='forgotusername'),
 	###
	# End UserAuth routes.
	###

	###
	# Admin Management Routes:
	#	adduser/
	#	updateuser/(:userid)/
	#	deleteuser/(:userid)/
	#	changepwd/(:userid)/
	###
	url(r'^adduser/', AdminManagement.adduser, name='adduser'),
	url(r'^updateuser(?:/(\d+))?/$', AdminManagement.updateuser, name='updateuser'),
	url(r'^deleteuser(?:/(\d+))?/$', AdminManagement.deleteuser, name='deleteuser'),
	url(r'^changeuserpwd(?:/(\d+))?/$', AdminManagement.changeuserpwd, name='changeuserpwd'),
	###
	# End Admin Management Routes.
	###

	###
	# Document Management General User Routes:
	#	viewdoc/(:documentid)/
	###
    url(r'^viewdoc(?:/(\d+))?/$', DocumentManagement.viewdoc, name='viewdoc'),
	###
	# End Document Management General User Routes.
	###

	###
	# Document Management Author Routes:
	#	adddocument/
	#	updatedocument/(:documentid)/
	###
    url(r'^adddocument/', DocumentManagementAuthor.adddocument, name='adddocument'),
    url(r'^updatedocument(?:/(\d+))?/$', DocumentManagementAuthor.updatedocument, name='updatedocument'),
	###
	# End Document Management Author Routes.
	###
)