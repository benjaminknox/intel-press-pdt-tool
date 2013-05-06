from django.contrib import admin
from dashboard.models import *

# Register your models here.
admin.site.register(Document)
admin.site.register(File)
admin.site.register(Meeting)
admin.site.register(Notification)
admin.site.register(Organization)
admin.site.register(Comment)