import calendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

#This class is a calendar of the meeting.
class MeetingCalendar(calendar.HTMLCalendar):

    #Initialize the class
    def __init__(self, meetings):
        #Load the class.
        super(MeetingCalendar, self).__init__()
        #Load the meetings.
        self.meetings = self.group_by_day(meetings)

    #Output the calendar with the information.
    def formatday(self, day, weekday):
        #Check the day
        if day != 0:
            #Get the css classes.
            cssclass = self.cssclasses[weekday]
            #Add a highlighter for this day.
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            #If there is a meeting on the day, highlight that day.
            if day in self.meetings:
                #Add the class that fills the day.
                cssclass += ' filled'
                #Add a list with links for the 
                #       meetings on that day.
                body = ['<ul>']
                #Loop through the meetings and 
                #       add them to the list.
                for meeting in self.meetings[day]:
                    #Open list tag.
                    body.append('<li>')
                    #Close the append tag.
                    body.append('<a href="javascript:view_meeting(\'%s\');" class="meeting_link" title="Click to view \'%s\'">'%(meeting.publicid,meeting.name))
                    #Output the meeting.
                    body.append(esc(meeting.name))
                    #Close the link and the list tag.
                    body.append('</a></li>')
                #Close the list.
                body.append('</ul>')
                #Return the day cell.
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            #Return the cssclass cell.
            return self.day_cell(cssclass, day)
        #Return just a normal cell.
        return self.day_cell('noday', '&nbsp;')

    #Format the month.
    def formatmonth(self, year, month):
        #Define the year and the month
        self.year, self.month = year, month
        #Create an instance of this month.
        return super(MeetingCalendar, self).formatmonth(year, month)

    #Get a list of the meetings in a given day.
    def group_by_day(self, meetings):
        #return the meeting
        field = lambda meeting: meeting.startdate.day
        #Return 
        return dict(
            [(day, list(items)) for day, items in groupby(meetings, field)]
        )

    #This is the day in the calendar.
    def day_cell(self, cssclass, body):
        #Return the day in the calendar.
        return '<td class="%s">%s</td>' % (cssclass, body)