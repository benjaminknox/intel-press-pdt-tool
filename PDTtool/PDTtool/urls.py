from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PDTtool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #The user management urls are included here.
    #	The urls contained this app are:
    #		login/
    #		logout/
    #		register/
    url(r'^', include('user_management.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
