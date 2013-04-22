from django.conf.urls import patterns, url

from document_management import views

"""
"Url Schema:
"   -login/
"   -add/
"   -(:documentid)/view/
"   -(:documentid)/delete/
"   -(:documentid)/(:locationid)/download/
"   -(:documentid)/approve/
"   -(:documentid)/addcomment/
"   -(:documentid)/(:commentid)/editcomment/
"   -(:documentid)/(:commentid)/deletecomment/
"""

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(\d+)/view/$', views.view, name='view'),
    url(r'^(\d+)/delete/$', views.delete, name='delete'),
    url(r'^(\d+)/approve/$', views.approve, name='approve'),
    url(r'^(\d+)/addcomment/$', views.addcomment, name='addcomment'),
    url(r'^(\d+)/(/d+)/download/$', views.download, name='download'),
    url(r'^(\d+)/(/d+)/editcomment/$', views.editcomment, name='editcomment'),
    url(r'^(\d+)/(/d+)/deletecomment/$', views.deletecomment, name='deletecomment'),
)
