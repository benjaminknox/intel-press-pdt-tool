from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PDTtool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #This is our base url.
    url(r'^', include('document_management.urls')),
    url(r'^admin/', include(admin.site.urls)),
)