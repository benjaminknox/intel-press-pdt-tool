from django.conf.urls import patterns, include, url

#This loads the admin site app.
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PDTtool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Load the urls for the main IntelPress PDT Portal app.
    url(r'^', include('dashboard.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
