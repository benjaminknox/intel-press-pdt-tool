from django.contrib import admin
from user_management.models import ExtendedUser, Notification, Organization, ActivateUserDB,ForgotPasswordDB

#These models get registered for CRUD
#	in the admin site.
admin.site.register(ExtendedUser)
admin.site.register(Notification)
admin.site.register(Organization)
admin.site.register(ActivateUserDB)
admin.site.register(ForgotPasswordDB)