from time import strptime,strftime
from topic_management.models import Topic

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