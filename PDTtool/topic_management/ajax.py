from django import http
from django.utils import simplejson
from topic_management import models as tm_models  
from topic_management import resources as tm_resources
from django.core.serializers.json import DjangoJSONEncoder

def topic_comments(request):
  if (
    'csrfmiddlewaretoken' not in request.POST or
    'topic_publicid'  not in request.POST
  ): return http.redirect("/")
  topic_object = tm_models.Topic.objects.get(publicid=request.POST['topic_publicid'])
  
  topic = tm_resources.get_topic(request,topic_object)
  context = {
    'topic':topic
  }

  #topic_comments_object = topic_object.comments.all()

  #topic_comments = list(topic_comments_object.values_list())

  # for comment in topic_comments_object:
  #  full_user_name = comment.user.get_full_name()
  # topic_comments[comment.id][2] = full_user_name

  #topic_json_object = simplejson.dumps(topic_comments,cls=DjangoJSONEncoder)

  #return http.HttpResponse(topic_json_object)

  
  return http.render(request,
    'topic_management/topic_comments.html',
    context)
  