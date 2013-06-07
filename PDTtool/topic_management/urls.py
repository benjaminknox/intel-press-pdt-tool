from django.conf.urls import patterns, url
from topic_management import views, ajax

urlpatterns = patterns('',

	#The addtopic script
	url(r'^addtopic/$', views.addtopic, name='addtopic'),

	#The viewtopics script
  url(r'^viewtopics/$', views.viewtopics, name='viewtopics'),

	#The viewtopic script
  url(r'^viewtopic/$', views.viewtopic, name='viewtopic'),

	#The download script
	url(r'^download/(.+)/(.+)$', views.download, name='download'),

  #Load the topic comments
  url(r'^topic_comments/$', ajax.topic_comments, name='topic_comments'),
    
)