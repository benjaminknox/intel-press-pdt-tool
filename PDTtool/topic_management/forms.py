from django import forms
from topic_management.models import Topic

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

  #These are the choices for the categories.
  choices = (
      ('Proposal','Proposal'),
      ('Outline','Outline'),
      ('Workbook','Workbook'),
      ('Book','Book'),
      ('Guest Visit','Guest Visit'),
      ('Opens','Opens'),
  )
  #This is the category.
  category = forms.ChoiceField(choices=choices)

class upload_document_form(forms.Form):
  file = forms.FileField(widget=forms.FileInput(attrs={'id':'file','class':'file_form'}))