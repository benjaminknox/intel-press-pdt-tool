from django.conf.urls import patterns, url
from user_management import views
urlpatterns = patterns('',
	
	# These urls are in UserAuth.
	
	#The login script. 
    url(r'^login/$', views.login, name='login'),

	#The logout script. 
    url(r'^logout/$', views.logout, name='logout'),

	#The register script. 
    url(r'^register/$', views.register, name='register'),

	#The register script. 
    url(r'^activate/$', views.activate, name='activate'),

    #The forgot password sequence
    url(r'^forgotpassword/$', views.forgotpassword, name='forgotpassword'),
	# End urls in UserAuth.
	
	
	# These urls are in user_management.
	
	#These are the account settings.
    url(r'^accountsettings/$', views.accountsettings, name='accountsettings'),
	
	#Reset the password.
    url(r'^resetpassword/$', views.resetpassword, name='resetpassword'),
	
	# End urls in user_management.
	
)