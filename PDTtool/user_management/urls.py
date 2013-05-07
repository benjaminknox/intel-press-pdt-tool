from django.conf.urls import patterns, url
from user_management import views

urlpatterns = patterns('',
	
	#The login script. 
    url(r'^login$', views.login, name='login'),

)