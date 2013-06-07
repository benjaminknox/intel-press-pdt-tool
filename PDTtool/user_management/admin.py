from django.contrib import admin
#from user_management.models import ExtendedUser, Notification, Organization, ActivateUserDB,ForgotPasswordDB
from user_management import models as um_models

#These models get registered for CRUD
#	in the admin site.
admin.site.register(um_models.ExtendedUser)
admin.site.register(um_models.UserNotifications)
admin.site.register(um_models.Organization)
admin.site.register(um_models.ActivateUserDB)
admin.site.register(um_models.ForgotPasswordDB)