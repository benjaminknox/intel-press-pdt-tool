from topic_management.models import Topic
from uuid import uuid4

def generate_topic_slug():

  unique=False
  
  while not unique:
    slug = str(uuid4())[:8]
    try:
      Topic.objects.get(topic_slug=slug)
    except:
      unique = True

  return slug