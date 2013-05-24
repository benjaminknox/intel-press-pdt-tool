from pdtresources.templates import topic_html
from topic_management.models import Topic
from meeting_management.models import Meeting
from django import forms #CheckboxSelectMultiple, ModelForm, TextInput
from django.utils.safestring import mark_safe

###
# This is the first step of the meeting form.
#			-This first step allows us to make a meeting form.
###
class MeetingFormStepOne(forms.ModelForm):
	#This is the meta class
	class Meta:
		#Load the model of the form.
		model = Meeting
		#Get the widgets
		widgets = {
			#This is the due date.
			'duedate': forms.TextInput(attrs={'class':'datepicker'}),
			#This is the start date.
			'startdate': forms.TextInput(attrs={'class':'datepicker'}),
			#This is the start date.
			'starttime': forms.TextInput(attrs={'class':'timepicker'}),
		}
		#These are the fields we need to
		#		get for the first form.
		fields = [
				  'name',
				  'description',
				  'duedate',
				  'startdate',
				  'starttime',
				  ]

 	#This initializes the form.
	def __init__(self, *args, **kwargs):
		#This is the super meeting.
		super(MeetingFormStepOne, self).__init__(*args, **kwargs)

		#We change the label of fields in the form.
		self.fields['name'].label = "Meeting Name"
		self.fields['duedate'].label = "Submission Cut Off Date"
		self.fields['startdate'].label = "Meeting Start Date/Time"


#This is the second step of the meeting form.
class MeetingFormStepTwo(forms.ModelForm):
	#This is the meta class
	class Meta:
		#Load the model of the form.
		model = Meeting
		#Get the widgets.
		widgets = {
			'topics': forms.CheckboxSelectMultiple(),
		}
		#Get the fields for this form.
		fields = [
				  'topics',
				  'duration',
				  ]


 	#This initializes
	def __init__(self, *args, **kwargs):
		#This is the super meeting.
		super(MeetingFormStepTwo, self).__init__(*args, **kwargs)

		#Change the label of the duration.
		self.fields['duration'].label = "Meeting Duration (hrs)"

		#Output the document fields to grab.
		self.fields['topics'].queryset = Topic.objects.filter(deleted=False)
		#Change the label of topics.
		self.fields['topics'].label = ''
		#Get the html from the templates.
		self.fields['topics'].label_from_instance = lambda obj: mark_safe(topic_html(obj))