from pdtresources.templates import topic_html
from topic_management.models import Topic
from meeting_management.models import Meeting
from django import forms #CheckboxSelectMultiple, ModelForm, TextInput
from django.utils.safestring import mark_safe

#This is the MeetingForm.
class MeetingForm(forms.ModelForm):
	#This is the Meta.
	class Meta:
		#This is the model that is loaded.
		model = Meeting
		#We exclude these fields.
		#exclude = ('user','deleted','scheduleitems','Usersattending')
		#This fields have special attributes here
		widgets = {
			'duedate': forms.TextInput(),
			'startdate': forms.TextInput(),
			'topics': forms.CheckboxSelectMultiple(),
		}
		fields = [
				  'name',
				  'topics',
				  'description',
				  'duration',
				  'maxscheduleitems',
				  'duedate',
				  'startdate',
				  ] 
	#This initializes
	def __init__(self, *args, **kwargs):
		#This is the super meeting.
			super(MeetingForm, self).__init__(*args, **kwargs)
		#Output the document fields to grab.
			self.fields['topics'].queryset = Topic.objects.filter(deleted=False)
			self.fields['topics'].label_from_instance = lambda obj: '{"topic_id":"'+str(obj.id)+'","topic_publicid":"'+str(obj.publicid)+'","topic_name":"'+obj.name+'","topic_user_first_name":"'+obj.user.first_name+'","topic_description":"'+obj.description+'"}' 

#This is the first step of the meeting form.
class MeetingFormStepOne(forms.ModelForm):
	#This is the meta class
	class Meta:
		#Load the model of the form.
		model = Meeting
		#Get the widgets
		widgets = {
			'duedate': forms.TextInput(attrs={'class':'datetimepicker'}),
			'startdate': forms.TextInput(attrs={'class':'datetimepicker'}),
		}
		fields = [
				  'name',
				  'description',
				  'maxscheduleitems',
				  'duedate',
				  'startdate',
				  ]

 	#This initializes
	def __init__(self, *args, **kwargs):
		#This is the super meeting.
		super(MeetingFormStepOne, self).__init__(*args, **kwargs)

		self.fields['name'].label = "Meeting Name"
		self.fields['maxscheduleitems'].label = "Amount of Topics to Review"
		self.fields['duedate'].label = "Submission Cut Off Date"
		self.fields['startdate'].label = "Meeting Start Date/Time"


#This is the second step of the meeting form.
class MeetingFormStepTwo(forms.ModelForm):
	#This is the meta class
	class Meta:
		#Load the model of the form.
		model = Meeting
		widgets = {
			'topics': forms.CheckboxSelectMultiple(),
		}
		fields = [
				  'topics',
				  'duration',
				  ]


 	#This initializes
	def __init__(self, *args, **kwargs):
		#This is the super meeting.
		super(MeetingFormStepTwo, self).__init__(*args, **kwargs)

		topic_div = lambda topic: topic_html(topic)

		self.fields['duration'].label = "Meeting Duration (hrs)"

		#Output the document fields to grab.
		self.fields['topics'].queryset = Topic.objects.filter(deleted=False)
		self.fields['topics'].label = ''
		self.fields['topics'].label_from_instance = lambda obj: mark_safe(topic_html(obj))
		"""self.fields['topics'].label_from_instance = lambda obj: '{"topic_id":"%s","topic_publicid":"%s","topic_name":"%s","topic_user_first_name":"%s","topic_description":"%s","topic_html":"%s"}'%(
						str(obj.id),
						str(obj.publicid),
						obj.name,
						obj.user.first_name,
						obj.description,
						topic_div(obj),

					)"""