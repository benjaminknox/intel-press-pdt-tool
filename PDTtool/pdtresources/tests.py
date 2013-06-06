from pdtresources.testsimplifier import Testsimplifier
#from django.test import TestCase
from meeting_management.models import Meeting
from pdtresources.MeetingsCalendar import MeetingCalendar
from datetime import date

class Pdtresources_TestCase(Testsimplifier):

  def test_meetingcalendar(self):

    today = date.today()
    year = today.year
    month = today.month

    #Load an empty calendar
    calendar = MeetingCalendar({}).formatmonth(year,month)

    #Test that the calendar loads the current calendar.
    self.assertIn('today',calendar)

    username = 'user.calendar'
    extuser = self.create_user(username,password='test')

    #Create a meeting to display on the calendar.
    meeting = Meeting(
                  name='Test Meeting',
                  description='Test Meeting Description',
                  duedate='%d-%d-12' % (year, month),
                  startdate = '%d-%d-15' % (year, month),
                  starttime = '13:00:00',
                  user = extuser.user,
                  maxscheduleitems=9,
                  duration=0,
              )

    #Save the meeting.
    meeting.save()

    calendar = MeetingCalendar(Meeting.objects.all()).formatmonth(year, month)

    #Test that the calendar loads the current calendar.
    self.assertIn('filled',calendar)

  #def test_comment_forms(self):
