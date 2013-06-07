import time
from django import http
from django import shortcuts
from django.utils import simplejson
from topic_management import models as tm_models
from topic_management import resources as tm_resources
from django.core.serializers.json import DjangoJSONEncoder

def comment_count(comment_object):
  comment_count_var = comment_object.count()
  for comment_thread in comment_object:
    comment_count_var += comment_count(comment_thread.comments.all())

  return comment_count_var

#def get_comments(comment_object):
#  return json_object

#This is the long poller
def topic_comments(request):

  get_topic_comments = lambda x:tm_models.Comment.objects.filter(topic__publicid=x)

  #Get the topic publicid.
  topic_publicid = request.GET['topic_publicid']

  #Get the topic.
  topic_object = get_topic_comments(topic_publicid)

  #Get the comment count.
  comment_count_var = comment_count(topic_object)

  i = 0
  #Wait for 20 seconds.
  while i < 10:

    #Get the comment count.
    current_comment_count = comment_count(get_topic_comments(topic_publicid))
    
    #for comment_thread in get_topic_comments():
    #  comment_thread_count

    #Get the topic comment count.
    if comment_count_var != current_comment_count:

      #json_object = simplejson(get_comments(topic_object),cls=DjangoJSONEncoder)

      topic = tm_models.Topic.objects.get(publicid=topic_publicid)
  
      topic = tm_resources.get_topic(request,topic)
      context = {
        'topic':topic
      }
      
      return shortcuts.render(request,
        'topic_management/topic_comments.html',
        context)
      

      #return http.HttpResponse("Topic Comment : %s" % json_object)


    #Increment the variable.
    i+= 1
    #Sleep the loop.
    time.sleep(2)

  return http.HttpResponse("9")