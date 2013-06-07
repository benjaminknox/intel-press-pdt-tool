from django import forms
from topic_management.models import Topic
from PDTtool import settings

"""
" The TopicForm class is a form for
"	uploading to the Topic class.
"
"	-Views: 'addtopic'
"
"""
class TopicForm(forms.Form):

  #The name of the document
  name = forms.CharField( max_length=255, required=True )

  #A short description of the document
  #   written by the uploader
  description = forms.CharField( widget=forms.Textarea )

  print settings.TOPIC_CATEGORIES

  topic_category_choices = []

  for category in settings.TOPIC_CATEGORIES:
    topic_category_choices.append((category,category,))

  #These are the choices for the categories.
  choices = topic_category_choices

  #This is the category.
  category = forms.ChoiceField(choices=choices)

class upload_document_form(forms.Form):
  file = forms.FileField(widget=forms.FileInput(attrs={'id':'file','class':'file_form'}))