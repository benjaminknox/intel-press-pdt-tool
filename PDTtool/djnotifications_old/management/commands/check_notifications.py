from django.core.management.base import BaseCommand, CommandError
from djnotifications.lib import check_notifications

#Run the command.
class Command(BaseCommand):
  #Run the handle.
  def handle(self, *args, **options):
    #Check the notifications
    check_notifications()