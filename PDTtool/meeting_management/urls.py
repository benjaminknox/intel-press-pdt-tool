from meeting_management import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.viewmeetings, name='viewmeetings'),
)