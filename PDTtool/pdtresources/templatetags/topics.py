from django import template
from topic_management.models import Topic
from django.template.loader import render_to_string

#Register the template library.
register = template.Library()

#Register the tag name into the templates.
@register.simple_tag(name="topics_by_category")

def topics_by_category(category):
  #Get the topics in the category.
  topics = Topic.objects.filter(category=category['name'],
                                readyforreview=True,
                                meeting = None,
                                deleted=False)

  #Predefine a return string.
  return_string = ""

  #Generate a context.
  context = {
    #Create the category.
    'category':{
      #Set the name
      'name':category['name'],
      'count':category['count']
    },
    'original':True
  }

  #Loop through the topics.
  for topic in topics:
    context['topic'] = topic
    return_string += render_to_string('meeting_management/topic_element.html',context)

  return return_string