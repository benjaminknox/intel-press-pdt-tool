from django.core.management.base import BaseCommand, CommandError
from djnotifications.lib import list_notifications

#Run the command.
class Command(BaseCommand):
  #Run the handle.
  def handle(self, *args, **options):
    #List the notifications
    list_notifications() 