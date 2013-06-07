#import re
import calendar
from itertools import groupby
from django.utils import simplejson
from datetime import date,datetime,timedelta
from schedule_management.models import CategorySchedule
from django.core.serializers.json import DjangoJSONEncoder
from schedule_management import resources as scheduleresources

from django.utils.html import conditional_escape as esc

#This class is a calendar of the meeting.
class MeetingCalendar(calendar.HTMLCalendar):

    #Initialize the class
    def __init__(self, meetings):
        #Load the class.
        super(MeetingCalendar, self).__init__(6)
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
                    #Get the meeting_name.
                    meeting_name = esc(meeting.name)
                    #Get the meeting owner user full name
                    meeting_owner_name = esc(meeting.user.get_full_name())
                    #Get the meeting topics.
                    schedule_topics = scheduleresources.get_meeting_schedule(meeting)
                    meeting_topics = schedule_topics['meeting_topics']
                    topics_list = schedule_topics['topics_list']
                    category_order = schedule_topics['category_order'] 
                    #Get the meeting scheduled topics count.
                    meeting_topic_count = len(meeting_topics)
                    #Check that the meeting topic count is greater than 0.
                    if meeting_topic_count > 0:
                        #Order the topics by the order they appear in the schedule.
                        topics = meeting_topics#.order_by('scheduleorder')
                        #Get an iterable list of the topics with all of the values
                        #topics_list = list(topics.values())
                        #print topics_list
                        #Create an incremental value.
                        i = 0
                        #Loop through the topics.
                        for topic in topics:
                            #Set the topics list presenter information to
                            #       the owner of the topics full name.
                            topics_list[i]['presenter'] = topic.user.get_full_name()
                            #Get an iterable list of all of the documents in the topic.
                            documents_list = list(topic.documents.all().values())
                            #Create a JSON for all of the, they will be passed into the DOM.
                            topics_list[i]['documents'] = simplejson.dumps(documents_list,cls=DjangoJSONEncoder)
                            #Increment i.
                            i += 1
                        #Create a JSON for the topics list, it will be passed into the DOM.
                        meeting_topics = simplejson.dumps(topics_list,cls=DjangoJSONEncoder)
                    else:#If there are no topics.
                        #Pass an empty string.
                        meeting_topics = ""

                    attr = 'class="meeting-item" '#Create a class attribute.
                    attr+= 'meeting-publicid="%s" ' % meeting.publicid#Pass in the meeting publicid to the DOM.
                    attr+= 'meeting-name="%s" ' % meeting_name#Pass in the meeting name to the DOM.
                    attr+= 'meeting-description="%s" ' % esc(meeting.description)#Pass in the meeting description to the DOM.
                    attr+= 'meeting-duedate="%s" ' % meeting.duedate#Pass inthe meeting duedate to the DOM.
                    attr+= 'meeting-duration="%s" ' % meeting.duration#Pass in the meeting duration.
                    attr+= 'meeting-startdate="%s" ' % meeting.startdate#Pass in the meeting startdate to the DOM.
                    attr+= 'meeting-starttime="%s" ' % meeting.starttime#Pass in the meeting starttime to the DOM.
                    attr+= 'meeting-ownername="%s" ' % meeting_owner_name#Pass in the meeting owner to the DOM.
                    attr+= 'meeting-topic-count="%s" ' % meeting_topic_count#Pass in the meeting topic count to the DOM.
                    attr+= 'meeting-topics=\'%s\' ' % esc(meeting_topics)#Pass in the meeting topics to the DOM.
                    attr+= 'title="\'%s\' has %s topic(s)"' % (meeting_name, meeting_topic_count) #Createa  title for the topics.
                    attr+= 'meeting-category-order=\'%s\'' % simplejson.dumps(category_order,cls=DjangoJSONEncoder)

                    #Open list tag, insert all of the attributes defined
                    #   above to the meeting information.
                    body.append('<li %s>' % attr)
                    #Append the meeting name to the list.
                    body.append(meeting_name);
                    #Close the link and the list tag.
                    body.append('</li>')
                #Close the list.
                body.append('</ul>')

                #Return the day cell.
                return self.day_cell(cssclass, '%s' % (''.join(body)),day)
                #return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)),day)
            #Return the cssclass cell.
            return self.day_cell(cssclass, '&nbsp;', day)
        #Return just a normal cell.
        return self.day_cell('noday', '&nbsp;', day)

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
    def day_cell(self, cssclass, body, day):

        #If it is not a day in the calendar
        #   month that is displayed.
        if not day:
            day = ''#Output the day.

        #Define cell wrapper classes.
        cell_wrapper_class = 'cell_wrapper cell_wrapper_selector'
        #Check to see if there is a highlight in the css class.
        if 'today' in cssclass: 
            #Add a highlight to the cell_wrapper_class.
            cell_wrapper_class += ' highlight'

        #Get the month_value
        month_value = "0%d" % self.month if len("%d" % self.month) == 1 else self.month

        #Get the date string
        date_string = "%s-%s-%s" % (self.year,month_value,day)

        #This is the day.
        if day != '':
            #Get the cut off date.
            cut_off_date = datetime.strptime(date_string, '%Y-%m-%d') - timedelta(days=3)
        else:
            #Set the cut off date as today.
            cut_off_date = datetime.now()

        #This is the date_string, it tells us when the date that is clicked.
        cut_off_date_string = "%s-%s-%s" % (cut_off_date.year,cut_off_date.month,cut_off_date.day)

        #This is the textual date that is listed when a user clicks on the form.
        date_textual_string = "%s %s, %s" % (calendar.month_name[self.month],day,self.year)

        #Place the date (format, and textual) into the DOM using these attributes.
        date_attr_string = 'date-value="%s" cut-off-date-value="%s" date-textual="%s"' % (date_string,
                                                                                          cut_off_date_string,
                                                                                          date_textual_string)

        #Create a cell.

        #Insert the css class and date information.
        cell = '<td class="%s" %s valign="top">' % (cssclass,date_attr_string)
        cell+= '<div style="position:relative">' #Add a wrapper with a relative position.
        cell+= '<div class="%s">'% cell_wrapper_class #Output the cell wrapper for styling.
        cell+= '<div class="cell_forms"></div><!-- .cell_forms -->' #Add in cell_form.
        cell+= '<span class="number">%s</span>' % day #Add a day.
        cell+= body #Add the body of the cell, it is a list of documents.
        cell+= '<div class="cell_info"></div><!-- .cell_info -->' #Get the cell_info.
        cell+= '</div><!-- classes: %s -->' % cell_wrapper_class #Close the cell wrapper classes.
        cell+= '</div>' #close the relative positon.
        cell+= '</td>'#Add in the css class.

        #Return the day in the calendar.
        return cell