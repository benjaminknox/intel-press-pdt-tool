from meeting_management.models import Meeting
from django import forms #CheckboxSelectMultiple, ModelForm, TextInput

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
			'duedate': forms.TextInput(attrs={'class':'stand_alone_datepicker'}),
			#This is the start date.
			'startdate': forms.TextInput(attrs={'class':'stand_alone_datepicker'}),
			#This is the start date.
			'starttime': forms.TextInput(attrs={'class':'stand_alone_timepicker'}),
			#This is the start date.
			'description': forms.Textarea(attrs={'class':'textarea'}),
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
		self.fields['startdate'].label = "Meeting Start Date"
		self.fields['starttime'].label = "Meeting Start Time"

class AddMeetingForm(MeetingFormStepOne):
	#This is the meta class
	class Meta:
		#Load the model of the form.
		model = Meeting
		#Get the widgets
		widgets = {
			#This is the due date.
			'duedate': forms.TextInput(attrs={'class':'datepicker2'}),
			#This is the start date.
			'startdate': forms.TextInput(attrs={'class':'datepicker2'}),
			#This is the start date.
			'starttime': forms.TextInput(attrs={'class':'timepicker2'}),
			#This is the start date.
			'description': forms.Textarea(attrs={'class':'textarea'}),
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