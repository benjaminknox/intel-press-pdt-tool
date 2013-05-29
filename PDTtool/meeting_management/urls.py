from meeting_management import views
from django.conf.urls import patterns, url

"""
" These are important, the /viewmeetings/ is the 
"   first screen a user sees when they login. It
"   is the root. of the website.
"""
urlpatterns = patterns('',
	 #View the meetings script, it is the base url.
    url(r'^$', views.viewmeetings, name='viewmeetings'),
    #View the meetings script.
    url(r'^viewmeetings/$', views.viewmeetings, name='viewmeetings'),

    url(r'^oldviewmeetings/$', views.oldviewmeetings, name='oldviewmeetings'),
    #Add a meeting script.
  # url(r'^addmeeting/$', views.addmeeting, name='addmeeting'),
)