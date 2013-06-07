from django.conf.urls import patterns, include, url
from PDTtool import long_poller

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PDTtool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # The user management urls are included here.
    #	The urls contained this app are:
    #		login/
    #		logout/
    #		register/
    #       accountsettings/
    #       resetpassword/
    #       
    url(r'^', include('user_management.urls')),

    # The meeting management urls.
    url(r'^', include('meeting_management.urls')),

    # The topic management urls are included here.
    #   The urls contained this app are:
    #       addtopic/
    #       viewtopics/
    #       viewtopic/
    #       download/
    url(r'^', include('topic_management.urls')),

    url(r'^admin/', include(admin.site.urls)),

     #The register script. 
    url(r'^long_poller_topic_comments/$', long_poller.topic_comments, name='topic_comments'),
)
