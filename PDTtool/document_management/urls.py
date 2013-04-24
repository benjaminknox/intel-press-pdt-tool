from django.conf.urls import patterns, url
from document_management import views

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
    url(r'^$', views.viewdocuments, name='viewdocuments'),
    url(r'^index/', views.viewdocuments, name='viewdocuments'),
    url(r'^viewdocuments/', views.viewdocuments, name='viewdocuments'),
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
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^forgotpwd/', views.forgotpwd, name='forgotpwd'),
    url(r'^forgotusername/', views.forgotusername, name='forgotusername'),
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
	url(r'^adduser/', views.adduser, name='adduser'),
	url(r'^updateuser/(\d+)/$', views.updateuser, name='updateuser'),
	url(r'^deleteuser/(\d+)/$', views.deleteuser, name='deleteuser'),
	url(r'^changeuserpwd/(\d+)/$', views.changeuserpwd, name='changeuserpwd'),
	###
	# End Admin Management Routes.
	###

	###
	# Document Management General User Routes:
	#	viewdoc/(:documentid)/
	###
    url(r'^viewdoc/(\d+)/$', views.viewdoc, name='viewdoc'),
	###
	# End Document Management General User Routes.
	###

	###
	# Document Management Author Routes:
	#	adddocument/
	#	updatedocument/(:documentid)/
	###
    url(r'^adddocument/', views.adddocument, name='adddocument'),
    url(r'^updatedocument/(\d+)/$', views.updatedocument, name='updatedocument'),
	###
	# End Document Management Author Routes.
	###

)