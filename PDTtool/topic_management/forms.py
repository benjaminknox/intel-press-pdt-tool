from django import forms
from topic_management.models import Topic

class MeetingForm(forms.ModelForm):

	#This initializes
	def __init__(self, *args, **kwargs):
		#This is the super meeting.
   		super(MeetingForm, self).__init__(*args, **kwargs)

		#Output the document fields to grab.
   		self.fields['topics'].queryset = Topic.objects.filter(deleted=False)
   		self.fields['topics'].label_from_instance = lambda obj: '{"topic_id":"'+str(obj.id)+'","topic_name":"'+obj.name+'","topic_user_first_name":"'+obj.user.first_name+'","topic_description":"'+obj.description+'"}' 


"""
" The TopicForm class is a form for
"	uploading to the Topic class.
"
"	-Views: 'addtopic'
"
"""
class TopicForm(forms.Form):

  #The name of the document
  name = forms.CharField( max_length=255 )

  #A short description of the document
  #   written by the uploader
  description = forms.CharField( widget=forms.Textarea )

  category = forms.CharField( max_length=255 )

class upload_document_form(forms.Form):
  file = forms.FileField(widget=forms.FileInput(attrs={'id':'file','class':'file_form'}))