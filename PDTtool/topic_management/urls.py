from django.conf.urls import patterns, url
from topic_management import views

urlpatterns = patterns('',

	#The addtopic script
	url(r'^addtopic/$', views.addtopic, name='addtopic'),

	#The viewtopics script
  url(r'^viewtopics/$', views.viewtopics, name='viewtopics'),

	#The viewtopic script
   url(r'^viewtopic/$', views.viewtopic, name='viewtopic'),

	#The download script
	url(r'^download/(.+)/(.+)$', views.download, name='download'),
    
)