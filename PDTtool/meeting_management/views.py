from datetime import date
#from django.db.models import Q
#from topic_management.models import Topic
from django.utils.safestring import mark_safe
from meeting_management.models import Meeting
from topic_management.models import Topic
from django.shortcuts import render, redirect
from dateutil.relativedelta import relativedelta
from pdtresources.MeetingsCalendar import MeetingCalendar
from pdtresources.templates import modal,form_modal
from meeting_management.forms import MeetingFormStepOne#, MeetingFormStepTwo
from django.contrib.auth.decorators import login_required#, user_passes_test
from meeting_management.resources import format_time, format_date, update_meeting_schedule

# Create your views here.
@login_required
def viewmeetings(request):

	#Update the meeting information, this updates just this information:
	#		-The name.
	#		-The description.
	#		-The start time.
	if 'update_meeting_information' in request.POST:
		
		#Get the meeting to edit.
		meeting_to_edit = Meeting.objects.get(publicid=request.POST['update_meeting_information'])
		
		#Update the meeting name.
		meeting_to_edit.name = request.POST['name']
		#Update the meeting description.
		meeting_to_edit.description = request.POST['description']
		#Update the meeting start time.
		meeting_to_edit.starttime =format_time(request.POST['starttime'])

		#Save the meeting.
		meeting_to_edit.save()

	#Update the meeting schedule order, the order is the right way.
	if 'update_meeting_schedule_publicid' in request.POST:

		#Get the meeting to edit.
		meeting_to_edit = Meeting.objects.get(publicid=request.POST['update_meeting_schedule_publicid'])

		#Get the schedule_items.
		schedule_items = request.POST['schedule_items'].split(',')
		#Update the meeting schedule.
		update_meeting_schedule(meeting_to_edit,schedule_items,new=False)
		#Update the items on the schedule.
		meeting_to_edit.maxscheduleitems = len(schedule_items)
		#Save the meeting information.
		meeting_to_edit.save()


	#Check for a meeting.
	if 'schedule_items' in request.POST and 'addmeetingform' in request.session:
		#Add the meeting form a session variable.
		form = request.session['addmeetingform']
		#Get the publicid for all of the topics.
		schedule_items = request.POST['schedule_items'].split(',')
		#Format the duedate.
		duedate = format_date(form['duedate'])
		#Format the startdate.
		startdate =  format_date(form['startdate'])
		#Get the starttime
		starttime = format_time(form['starttime'])
		#Create a new meeting.
		newmeeting = Meeting(
											name = form['name'],
											description=form['description'],
											duedate=duedate,
											startdate=startdate,
											maxscheduleitems=len(schedule_items),
											starttime=starttime,
											user=request.user,
											duration=0
		)
		#Save the new meeting.
		newmeeting.save()
		#Add Schedule
		update_meeting_schedule(newmeeting,schedule_items);

		#Redirect to the meetings 
		return redirect('/viewmeetings/')

	#Get the date of this month.
	today = date.today() + relativedelta(day=1)

	#Get the year of the current month.
	year = int(request.GET['year']) if 'year' in request.GET else today.year
	#Get the month.
	month = int(request.GET['month']) if 'month' in request.GET else today.month
	#The date that will be displayed.
	displaydate = date(day=1,month=month,year=year)
	#Get the previous month.
	prev_month = displaydate+relativedelta(months=-1)
	#Get the next month.
	next_month = displaydate+relativedelta(months=+1)

	#Load the meeting objects into a list
	meetings = Meeting.objects.filter(
										  deleted=False,
										  startdate__year=displaydate.year,
										  startdate__month=displaydate.month,
										  )

	#Get the calendar.
	cal = MeetingCalendar(meetings).formatmonth(year, month)

	#load the topics available
	topics = Topic.objects.filter(meeting=None,
																readyforreview=True,
																supervisor_released=False,
																deleted=False)

	#Meeting Data
	meetings = [{
			#Get the meeting
			'meeting':m,
			#Get the publicid
			'publicid':m.publicid,
			#Get the view meeting modal.
			'meeting_view': mark_safe(
								#Load the modal.
								modal(request, mark_safe(
										#Load the meeting management template.
										render(request,
											'meeting_management/viewmeeting.html',
											#Pass in a context.
											{'meeting':m}
										#This simply means return the html
										).content 
									),
									#Add a title to the modal.
									modal_title="%s at %s" % (m.name,m.startdate),
									#Change the modal.
									modal_id=m.publicid
								).content
							),
				#Get the meeting form to edit.
				'edit_meeting_form1':form_modal(request,
									#Add the meeting form.
									'editmeetingform_%s'%m.publicid,
									#Get the actual form from the form model.
									MeetingFormStepOne({
										'name':m.name,
										'description':m.description,
										'duedate':m.duedate,
										'startdate':m.startdate,
										'starttime':m.starttime,
									}).as_table(),
									#Name the modal_form.
									table_class='modal_form',
									#Add the topics.
									submit_text='Update',
									#Add a modal title.
									modal_title='Edit \'%s\'' % m.name,
									#Add a modal_id.
									modal_id='editmeetingform1_%s' % m.publicid,
									#Add an extra field html.
									extra_fields='<input type="hidden" name="update_meeting_information" value="%s"/>' % m.publicid
								),
				#Get the schedule editor for this interface.
				'edit_meeting_form2':mark_safe(
						#Load a modal template 
						modal(request,
								#Get the schedule editor, this is the drag and drop for the meetingform.
								mark_safe(render(request,
													#This is the template name.
													'meeting_management/addmeetingform2.html',
													{
														#Add the topics that are in the meeting.
														'topics':topics,
														#Add the topics scheduled.
														'topics_scheduled':m.topics.all(),
														#Get the meeting.
														'meeting':m
													}).content
										),
								#Add the modal title.
								modal_title='Create a Schedule',
								#Add the modal id.
								modal_id='editmeetingform_%s' % m.publicid,
								#Add a class to the modal.
								modal_class='addmeetingform'
						).content
					),
		}
		for m in meetings
	]

#	topics_ready_count = len(Topic.objects.filter(,deleted=False))

	#Load the addmeeting form.
	if 'loadprevious' not in request.GET and 'loadnext' in request.GET and (
			#Check for meeting information in a form
			('addmeetingform' in request.session) 
				or
			#Check for the meeting in the add form.
			('addmeetingform' in request.POST)
		):
		
		#Save the post data in to a session variable
		request.session['addmeetingform'] = request.POST

		#Add a meeting form.
		addmeetingform2 = mark_safe(render(request,
														'meeting_management/addmeetingform2.html',
														{'topics':topics}).content
											)
		#Check the meeting form.
		meetingform = mark_safe(
				#Load a modal template 
				modal(request,
						#This is the meetingform.
						addmeetingform2,
						#This is the modal title.
						modal_title='Create a Schedule',
						#This is the add meeting form.
						modal_id='addmeetingform',
						#Add a class to the modal.
						modal_class='addmeetingform'
				).content
			)
		#Load the form.
		loadform = True
	else:
		#Load the form.
		loadform = True if 'loadprevious' in request.GET else False

		#If the form is the meeting form.
		if not loadform and 'addmeetingform' in request.session:
			#Delete the meeting.
			del request.session['addmeetingform']

		#Get the first meeting form
		meetingform = form_modal(request,
										#Add the meeting form.
										'addmeetingform',
										#Get the actual form from the form model.
										MeetingFormStepOne(
												#If there is request POST information,
												#			populate the form with it.
												request.POST if 'addmeetingform' in request.POST else 
													#If there is session from the previous form populate the form with it.
													#		otherwise the form can be empty.
													request.session['addmeetingform'] if 'addmeetingform' in request.session else None
										 ).as_table(),
										#Name the modal_form.
										table_class='modal_form',
										#Add the topics.
										submit_text='Add Topics',
										#Add a get string
										get_string='loadnext=1',
										#Add a modal title.
										modal_title='Add a Meeting',
										#Add a modal_id.
										modal_id='addmeetingform1'
									)

	#This is the context
	context = {
		#This is the title of the page.
		'title':'Meetings Calendar',
		#This is the display date.
		'displaydate':displaydate,
		#This is the previous month.
		'prev_month':prev_month,
		#This is a textual version of the previous month.
		'prev_month_textual':prev_month.strftime("%b, %Y"),
		#This is the next month.
		'next_month':next_month,
		#This is a textual version of the next month.
		'next_month_textual':next_month.strftime("%b, %Y"),
		'meetings':meetings,
		#Get the calendar
		'calendar':mark_safe(cal),
		#Get the meeting form
		'meetingform':meetingform,
		#Load the meeting form
		'loadform':loadform,
		}

	#Render the request information.
	return render(request,
 			'meeting_management/viewmeetings.html',
			context)