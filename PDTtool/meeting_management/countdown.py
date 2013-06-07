from meeting_management.models import Meeting

def meeting_start(meeting_publicid=None):

  meeting = Meeting.objects.filter(publicid=meeting_publicid)

  if meeting.count() == 0:
    print "This meeting doesn't exist."
    return False



  '''
  -1 Week before a meeting.
    -Notify who:
      -Anybody who owns a topic that is in the meeting.
      -The owner of the meeting.

  -3 days before a meeting.
    -Notify who:
      -Anybody who owns a topic that is in the meeting.
      -The owner of the meeting.

  -2 days before a meeting.
    -Notify who:
      -Anybody who owns a topic that is in the meeting.
      -The owner of the meeting.

  -1 day before a meeting.
    -Notify who:
      -Anybody who owns a topic that is in the meeting.
      -The owner of the meeting.
  '''
  pass


def countdown_notification():
  '''
  -Basically timebound notifications up until the cut off date,
    we email everyone in the system:
    -1 week before the cut off.
    -3 days before the cut off.
    -2 days before the cut off.
    -1 day before the cut off.
  '''
  pass