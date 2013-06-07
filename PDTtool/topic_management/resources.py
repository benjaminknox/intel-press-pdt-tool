from uuid import uuid4
from topic_management.models import Topic
from pdtresources.comments import recursive_comments, comment_form

def generate_topic_slug():

  unique=False
  
  while not unique:
    slug = str(uuid4())[:8]
    try:
      Topic.objects.get(topic_slug=slug)
    except:
      unique = True

  return slug

def get_topic(request,topic_object):
  #Get the topic
  topic = {
    #Store the topic_object
    'topic_object':topic_object,
    #Get the comments
    'comments':[
      #Get the comments for the topic
      {'html':str(recursive_comments(request, comment.publicid))}
      #Run a loop on the comments.
      for comment in topic_object.comments.all() 
    ],
    #Get the comment form for the topic.
    'comment_form':comment_form(request,'topic',topic_object.publicid),
  }

  return topic