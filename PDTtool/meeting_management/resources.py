from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from time import strptime,strftime
from topic_management.models import Topic
from meeting_management.models import Meeting
from schedule_management import resources as scheduleresources

def loadattendees(meeting=None,
                  meeting_pk=None,
                  meeting_publicid=None):

    if not meeting and not meeting_pk and not meeting_publicid:
        print "Please provide a meeting"
        return False

    if meeting_pk:
        meeting = Meeting.objects.filer(pk=meeting_pk)[0]

    if meeting_publicid:
        meeting = Meeting.objects.filer(pk=meeting_publicid)[0]

    attendees = list(meeting.attendees.all())
    meeting_topics = Topic.objects.filter(meeting=meeting).prefetch_related('user__extendeduser')

    for topic in meeting_topics:
        extuser = topic.user.extendeduser
        if extuser not in attendees: 
            attendees.append(extuser)

    return attendees

###
# This is the format of the date, the date for django has to be yyyy-mm-dd,
#   so this reformats the string passed by jQuery.
###
def format_date(thedate):
    #Format the date properly, this takes the month variables
    #   and adds a 0 if it is one character long.
    format_date = lambda t: '0'+ t if len(t) == 1 else t
    #Add the format of the date back.
    formatteddate = '-'.join([format_date(t) for t in thedate.split('-')])
    #Format the duedate into django format for a string.
    return formatteddate

###
# This is the format of the time, django is looking for this: 24:55:00
###
def format_time(thetime):
  return strftime('%H:%M:%S',strptime(('0'+thetime if len(thetime) == 6 
                            else thetime).upper(),
                          '%I:%M%p'))

###
# This updates a meeting schedule, if the meeting is new we 
#       need to create a new schedule.
###
def update_meeting_schedule(meeting,schedule_items,categories=None,new=True):
    pass
'''
    #If the meeting is not new we need to 
    #   clear the topics m2m list, it will 
    #   be repopulated a few lines later.
    if not new:
        #Have to update the topics meeting to 
        #   None so we can select it again.
        for topic in meeting.topics.all():
            #Set topic.meeting to None.
            topic.meeting = None
            #Save the topic
            topic.save()
        #Clear the topics from the schedule.
        meeting.topics.clear()

    #Increment a variable.
    i = 0
    #Loop through the itemes.
    for publicid in schedule_items:
        #Increment the count.
        i += 1
        #Check to make sure the publicid is not null.
        if publicid:
            #Get the topic based on the publicid.
            topic = Topic.objects.get(publicid=publicid)
            #Get the topic schedule order.
            topic.scheduleorder = i
            #Add the meeting to the topic.
            topic.meeting = meeting
            #Save the topic.
            topic.save()
            #Add the topic to the meeting.
            meeting.topics.add(topic)
    #Save the meeting.
    meeting.save()
'''

#This is the next meeting.
def get_next_meeting():
    #This is the current datetime.
    nowdate = datetime.now()
    #This the current time.
    nowtime = datetime.time(nowdate)

    #Load the next meeting.
    nextmeeting = Meeting.objects.filter(

      Q(startdate__gt=nowdate) |
        Q(startdate__gte=nowdate) &
        Q(starttime__gte=nowtime)

    ).order_by('startdate','starttime')

    #Check the count of the meeting.
    if nextmeeting.count() > 0:
        #If there is a meeting return the
        #   first meeting in the QuerySet.
        return nextmeeting[0]
    else:
        #Otherwise return nothing.
        return None

#################################################
# function isSupervisor: Check to see if the 
#                           user is a supervisor.
#       Requires: requst = a request object.
def IsSupervisor(request):
    #Check to see if the request.user is a Supervisor.
    if request.user.groups.filter(Q(name='Supervisor')).count() != 0:
        #If they are:
        return True

    #If they are not:
    return False

###############################################################
# function meeting_url_string: Creates a url to a particular 
#                                   meeting with the date included.
#       Requires: meetingpublicid = (String) The publicid for the
#                                   meeting_management.models.Meeting object.
#       Argument: special_vars = (Dictionary) Each iter is a 
#                                   get variable on the end of the string.
def meeting_url_string(meetingpublicid,special_vars=False):
    #Get a meeting_management.models.Meeting from the publicid.
    meeting = Meeting.objects.get(publicid=meetingpublicid)
    #Get the month from the meeting startdate.
    month = meeting.startdate.month
    #Get the year from the meeting startdate.
    year = meeting.startdate.year
    #Define an empty varstring.
    varstring = ""
    #Check if there are special_vars.
    if special_vars:
        #Loop through the special variables.
        for v in special_vars:
            #Create a string for the get variables
            varstring += "&%s=%s"%(v[0],v[1])
    #Check if a meeting has been deleted.
    if '&deleted=' not in varstring:
        #If not then add a meeting publicid in the hash.
        publicid_hash = '#'+meeting.publicid
    else:
        #If so then don't add a meeting public id.
        publicid_hash = ""

    #Generate a url to view the meeting.
    url = '/viewmeetings/?month=%d&year=%d%s%s'%(month,year,varstring,publicid_hash)

    #Return the url.
    return url

######################################################################
# function get_available_meetings: Gets the duration of meetings before the cut off 
#                                   date meetings in the system and returns the 
#                                   meetings that have space left.
def get_available_meetings():

  #Get the date right now.
  daterightnow = timezone.now()
  #Extract the time from the daterightnow.
  timerightnow = daterightnow.time()
  #Extract the date from the daterightnow.
  datewithouttime = daterightnow.date()

  #Get all of the meetings that are in the future.
  all_meetings = Meeting.objects.filter(
                                    deleted=False,
                                    duedate__gte=datewithouttime,
                                    startdate__gte=datewithouttime
                                    )

  #Create a list to return all of the meetings.
  meetings = []

  #Create a loop to through all of the meetings in the queryset.
  for meeting in all_meetings:

    if (#Check if the meeting start time and date are not in the past.
        (meeting.starttime >= timerightnow and
         meeting.startdate >= datewithouttime)
      or
        #If the meeting is not today it is in the future.
        (meeting.startdate > datewithouttime)
       ):

      #Convert the meeting duration which is in hours to minutes.
      meeting_duration_in_minutes = meeting.duration

      #Get the current meeting length from the meeting duration specified
      #     by the user that created the meeting.
      current_meeting_length = int(meeting_duration_in_minutes) - meeting.currentlength

      #Check that there is time left in the current meeting length.
      if current_meeting_length > 0:
        #Create a new property to pass the meeting lenght into the html page.
        meeting.current_meeting_length = current_meeting_length
        #Append the meeting to the end of the list to return.
        meetings.append(meeting)

  #Return the meeting list.
  return meetings

'''
"""
" This Code isn't being used anymore.
"""
from pdtresources.templates import form_modal
from django.utils.safestring import mark_safe
from meeting_management.forms import MeetingFormStepOne
from django.shortcuts import render

#Get the first meeting information form
def edit_meeting_form1(request, meeting):
    
    #Load Meeting Form StepOne
    form = MeetingFormStepOne({
                                'name':meeting.name,
                                'description':meeting.description,
                                'duedate':meeting.duedate,
                                'startdate':meeting.startdate,
                                'starttime':meeting.starttime,
                            }).as_table()

    #Get the modal_content.
    modal_content = form_modal(request,
                                #Add the meeting form.
                                'editmeetingform_%s'%meeting.publicid,
                                #Get the actual form from the form model.
                                form,
                                #Name the modal_form.
                                table_class='modal_form',
                                #Add the topics.
                                submit_text='Update',
                                #Add a modal title.
                                modal_title='Edit \'%s\'' % meeting.name,
                                #Add a modal_id.
                                modal_id='editmeetingform1_%s' % meeting.publicid,
                                #Add an extra field html.
                                extra_fields='<input type="hidden" name="update_meeting_information" value="%s"/>' % meeting.publicid,
                                #Add a special form action
                                action="%s#%s"% (request.get_full_path(),meeting.publicid)
                            )

    #Createa "safe" version of the modal content
    edit_meeting_form1 = mark_safe(modal_content)

    #Return the modal.
    return edit_meeting_form1

#Get the second meeting information.
def edit_meeting_form2(request,topics,meeting):
    #Load the view for.
    view = render(request,
            #This is the template name.
            'meeting_management/addmeetingform2.html',
            {
                #Add the topics that are in the meeting.
                'topics':topics,
                #Add the topics scheduled.
                'topics_scheduled':meeting.topics.all().order_by('scheduleorder'),
                #Get the meeting.
                'meeting':meeting
            }).content

    #Put the view into a modal.
    modal_content = modal(request,
        #Get the schedule editor, this is the drag and drop for the meetingform.
        mark_safe(view),
        #Add the modal title.
        modal_title='Create a Schedule',
        #Add the modal id.
        modal_id='editmeetingform_%s' % meeting.publicid,
        #Add a class to the modal.
        modal_class='addmeetingform'
    ).content

    #Edit the second meeting form.
    edit_meeting_form2 = mark_safe(modal_content)

    return edit_meeting_form2

#Get the next meeting information.
def view_meeting(request,meeting):
    #Load the meeting view.
    view = render(request,
        'meeting_management/viewmeeting.html',
        #Pass in a context.
        {
            'meeting':meeting,
            'topics':meeting.topics.order_by('scheduleorder')
        }
    #This simply means return the html
    ).content

    mstartdate = meeting.startdate
    mstarttime = meeting.starttime

    textualdate = "%s %d at %s" % (
                                 mstartdate.strftime('%B'),
                                 mstartdate.day,
                                 mstarttime.strftime('%I:%M %p').lstrip("0").replace('AM','a.m.').replace('PM','p.m.')
                                )

    #Put the view into a modal.
    modal_content = modal(request,
     mark_safe(view),
        #Add a title to the modal.
        modal_title="%s, %s" % (meeting.name,textualdate,),
        #Change the modal.
        modal_id=meeting.publicid
    ).content
    #Create the modal.
    view_meeting = mark_safe(modal_content)

    return view_meeting
'''