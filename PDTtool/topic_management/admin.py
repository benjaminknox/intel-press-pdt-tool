from django.contrib import admin
from topic_management.models import Topic, Document, Comment

admin.site.register(Topic)
admin.site.register(Document)
admin.site.register(Comment)