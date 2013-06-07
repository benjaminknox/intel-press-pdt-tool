from django.db.models import Q
from topic_management.models import Topic
from meeting_management.models import Meeting
from schedule_management.models import CategorySchedule
from django.utils import timezone

#A meeting has a schedule, we know a topic 
#  is in a meeting schedule because of the
#  foreignkey to a meeting.
#We know the order of the topic based on 
#  scheduleorder field. 
#A topic has a category, and the topic is
#  ordered by category also. So the 
#  scheduleorder field is by topic category.

def remove_from_schedule(topic):
  category_schedule = CategorySchedule.objects.filter(topics=topic)
  for schedule in category_schedule:

    schedule.currentlength = schedule.currentlength - topic.presentationlength
    schedule.save()
    
    meeting = topic.meeting
    meeting.currentlength = meeting.currentlength - schedule.currentlength
    meeting.save()

    topic.meeting = None
    topic.save()

    schedule.topics.remove(topic)

def get_meeting_schedule(meeting,schedules=None):
  schedule_category_objects = {}
  meeting_topics = []
  topics_list = []
  category_order = []

  if not schedules:
    schedules = CategorySchedule.objects.filter(meeting=meeting,deleted=False)

  for schedule in schedules:
    schedule_category_objects[schedule.category] = schedule
    schedule_topics = schedule.topics.all().order_by('category','scheduleorder')
    for topic in schedule_topics:
      meeting_topics.append(topic)

    for topic in schedule_topics.values():
      topics_list.append(topic)

    category_order.append((schedule.category,schedule.schedulecategoryorder))

  ret = {
    'schedule_category_objects': schedule_category_objects,
    'meeting_topics':meeting_topics,
    'topics_list':topics_list,
    'category_order':category_order
  }

  return ret

def delete_meeting_schedule(meeting):

  #Get the schedules
  schedules = CategorySchedule.objects.filter(meeting=meeting,deleted=False)
  
  #Get the topics associated with the meeting.
  #meeting_topics = meeting_to_delete.topics
  meeting_topics = get_meeting_schedule(meeting=meeting,schedules=schedules)['meeting_topics']
  
  #Loop through all of the meeting topics
  for t in meeting_topics:
    #Set the meeting to None.
    t.meeting = None
    #Save the meeting.
    t.save()
    #Go into the schedule.
    for schedule in schedules:
      #Remove the topic from the schedule.
      schedule.topics.remove(t)

  #Delete the schedules.
  schedules.delete()


def save_meeting_schedule(meeting,schedule_items,schedule_categories,new_meeting=False):

  if not new_meeting: delete_meeting_schedule(meeting)

  categories = {}
  i = 1
  for category in schedule_categories:
    if category != '':
      category_schedule = CategorySchedule(meeting=meeting,
                                           category=category,
                                           schedulecategoryorder = i
                                          )
      category_schedule.save()

      categories[category] = {

                              'category_object':category_schedule,
                              'topic_order': 1,
                              'currentlength': 0
                              }
      i += 1

  topics_list = []

  topic_order_dict = {}

  for topic_list in schedule_items:
    if topic_list:
      topic = topic_list.split('::::')
      topics_list.append(topic[1])
      topic_order_dict[topic[1]] = topic[0]

  topics = Topic.objects.filter(publicid__in=topics_list)

  print topic_order_dict

  meetingcurrentlength = 0

  for topic in topics:
    category_name = topic.category.lower().replace(' ','-')
    category = categories[category_name]
    category_object = category['category_object']
    category_object.topics.add(topic)
    topic.meeting = meeting
    topic.scheduleorder = topic_order_dict[topic.publicid]
    topic.save()

    topiclength = int(topic.presentationlength)
    category['currentlength'] += topiclength

    meetingcurrentlength += topiclength

  meeting.currentlength = meetingcurrentlength
  meeting.timeleft = meeting.duration - meetingcurrentlength
  meeting.save()

  for key,category in categories.iteritems():

    category['category_object'].currentlength = int(category['currentlength'])
    category['category_object'].save()

  #for key, schedulecategory in categories.iteritems():


def automatic_scheduler(topic=None, preferredmeeting=None):
  
  if topic:
    topics = Topic.objects.filter(publicid=topic)
  else:
    topics = Topic.objects.filter(deleted=False,
                                  readyforreview=True,
                                  supervisor_released=False,
                                  meeting=None
                                  )

  for topic in topics:
    #Get the preferred meeting.
    if preferredmeeting: 
      meeting = Meeting.objects.filter(
                                    publicid=preferredmeeting)
    else:
      now = timezone.now()
      meeting = Meeting.objects.filter(deleted=False,
                                      timeleft__gte=topic.presentationlength,
                                      duedate__gte=now).order_by(
                                        '-startdate')

    if meeting.count() > 0:
      add_topic_to_meeting(meeting[0], [topic,])

def add_topic_to_meeting(meeting,topics):
  
  #Get the categories in the meeting.
  category_objects = get_meeting_schedule(meeting)['schedule_category_objects']

  schedule_categories = []
  schedule_items = []
  category_topic_lists = {}

  #Loop through and get the current list of topics in each schedule.
  for key,category in category_objects.iteritems():
    if key not in category_topic_lists: category_topic_lists[key] = []
    for topic in category.topics.all():
      category_topic_lists[key].append(topic.publicid)

  for topic in topics:
    category_code_name = topic.category.lower().replace(' ','-')
    publicid = topic.publicid

    if publicid not in category_topic_lists[category_code_name]:
      category_topic_lists[category_code_name].append(publicid)

  for key, value in category_topic_lists.iteritems():
    schedule_categories.append(key)
    i = 1
    for topic_publicid in value:
      schedule_items.append('%s::::%s'%(i,topic_publicid))
      i += 1

  save_meeting_schedule(meeting,schedule_items,schedule_categories)

      #  topic.meeting = meeting
      #  topic.save()

'''
def update_meeting_schedule():
  pass

#When we append to a schedule we simple place it at the 
def append_to_schedule(meeting=None, topic=None):

  if not meeting and not topic: return False

  category = topic.category
  meeting_topics = Meeting.objects.all()

def push_to_schedule(meeting=None, topic=None):
  pass

'''