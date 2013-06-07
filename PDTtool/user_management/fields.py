from PDTtool import settings
from django.db import models
from south.modelsinspector import add_introspection_rules

class NotificationField(models.BooleanField):

  description = "A boolean field with a new argument called 'set_name' for layout."

  def __init__(self, set_name=settings.NOTIFICATION_SETS['main_set'],*args, **kwargs):

    self.set_name = set_name

    super(NotificationField, self).__init__(*args,**kwargs)

add_introspection_rules([
    (
        [NotificationField], 
        [],         
        {           
            "set_name": ["set_name", {"default": settings.NOTIFICATION_SETS['main_set']}],
        },
    ),
], ["^user_management\.fields\.NotificationField"])

