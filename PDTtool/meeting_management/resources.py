from datetime import datetime
from django.db.models import Q
from time import strptime,strftime
from pdtresources.templates import form_modal, modal
from topic_management.models import Topic
from meeting_management.models import Meeting
from django.utils.safestring import mark_safe
from meeting_management.forms import MeetingFormStepOne
from django.shortcuts import render

"""
" These are functions for meeting management, they
"       are used to minimize code duplication.
"""

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
def update_meeting_schedule(meeting,schedule_items,new=True):

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
    #Add an integer for the duration.
    duration = 0
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
            #Add the duration to the meeting.
            duration += topic.presentationlength
    #Add a new meeting in the duration.
    meeting.duration = duration
    #Save the meeting.
    meeting.save()

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

    if nextmeeting.count() > 0:
        return nextmeeting[0]
    else:
        return False

#Get the first meeting information form
def edit_meeting_form1(request, meeting):
    
    form = MeetingFormStepOne({
                                'name':meeting.name,
                                'description':meeting.description,
                                'duedate':meeting.duedate,
                                'startdate':meeting.startdate,
                                'starttime':meeting.starttime,
                            }).as_table()


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

    edit_meeting_form1 = mark_safe(modal_content)

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

    #Put the view into a modal.
    modal_content = modal(request,
     mark_safe(view),
        #Add a title to the modal.
        modal_title="%s at %s" % (meeting.name,meeting.startdate),
        #Change the modal.
        modal_id=meeting.publicid
    ).content
    #Create the modal.
    view_meeting = mark_safe(modal_content)

    return view_meeting