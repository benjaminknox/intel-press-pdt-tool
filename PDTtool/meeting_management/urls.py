from meeting_management import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
	#View the meetings script, it is the base url.
    url(r'^$', views.viewmeetings, name='viewmeetings'),
    #View the meetings script.
    url(r'^viewmeetings/$', views.viewmeetings, name='viewmeetings'),
    #Add a meeting script.
  # url(r'^addmeeting/$', views.addmeeting, name='addmeeting'),
)