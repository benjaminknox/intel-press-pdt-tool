from django.contrib import admin
from djnotifications.models import Notification, Task_argument

# Register your models here.
admin.site.register(Notification)
admin.site.register(Task_argument)