from django.db.models import Q
from datetime import date, datetime
#from topic_management.models import Topic
from topic_management.models import Topic
from django.utils.safestring import mark_safe
from meeting_management.models import Meeting
from django.shortcuts import render, redirect
from dateutil.relativedelta import relativedelta
from pdtresources.MeetingsCalendar import MeetingCalendar
from pdtresources.templates import modal,form_modal
from meeting_management.forms import MeetingFormStepOne, AddMeetingForm#, MeetingFormStepTwo
from django.contrib.auth.decorators import login_required#, user_passes_test
from meeting_management.resources import format_time, format_date, update_meeting_schedule, get_next_meeting, edit_meeting_form1, edit_meeting_form2, view_meeting

@login_required
def viewmeetings(request):

	"""
	" Generate the handlers for all of the data.
	"""

	"""
	" Handle the update of the meeting information.
	"""
	#Update the meeting information, this updates just this information:
	#		-The name.
	#		-The description.
	#		-The start time.
	if 'update_meeting_information' in request.POST:
		#Update this publicid
		publicid = request.POST['update_meeting_information']
		#Get the meeting to edit.
		meeting_to_edit = Meeting.objects.get(publicid=publicid)
		#Update the meeting name.
		meeting_to_edit.name = request.POST['name']
		#Update the meeting description.
		meeting_to_edit.description = request.POST['description']
		#Update the meeting start time.
		meeting_to_edit.starttime =format_time(request.POST['starttime'])

		#Save the meeting.
		meeting_to_edit.save()

		return redirect('/viewmeetings/?updated=%s#%s'%(meeting_to_edit.name,publicid))

	"""
	" End the handle of updating meeting information.
	"""

	"""
	" Handle the update of the schedule for each meeting.
	"""

	#Update the meeting schedule order, the order is the right way.
	if 'update_meeting_schedule_publicid' in request.POST:
		
		#Update this publicid
		publicid = request.POST['update_meeting_schedule_publicid']

		#Get the meeting to edit.
		meeting_to_edit = Meeting.objects.get(publicid=publicid)

		#Get the schedule_items.
		schedule_items = request.POST['schedule_items'].split(',')
		#Update the meeting schedule.
		update_meeting_schedule(meeting_to_edit,schedule_items,new=False)
		#Update the items on the schedule.
		meeting_to_edit.maxscheduleitems = len(schedule_items)
		#Save the meeting information.
		meeting_to_edit.save()

		return redirect('/viewmeetings/?updated=%s#%s'%(meeting_to_edit.name,publicid))

	"""
	" End the handle of the update of the schedule for this meeting.
	"""

	"""
	" Handle the add meeting form data.
	"""
	#This handles the information for the add meeting form.
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
		return redirect('/viewmeetings/?added=%s#%s'%(newmeeting.name,newmeeting.publicid))

	"""
	" End the handle of the add meeting form.
	"""

	"""
	" End the handlers of the data.
	"""

	"""
	" Generate the dates needed for the calendar interface.
	"""
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
	"""
	" End of calendar dates needed.
	"""


	"""
	" Get the meetings that will be on the calendar.
	"""
	#Load the meeting objects into a list
	meetings = Meeting.objects.filter(
										  deleted=False,
										  startdate__year=displaydate.year,
										  startdate__month=displaydate.month,
										  ).order_by('startdate','starttime')
	"""
	" End of the meetings that will be on the calendar.
	"""


	"""
	" For each meeting get the views asociated.
	"""
	#load the topics available, for making the schedule.
	topics = Topic.objects.filter(meeting=None,
																readyforreview=True,
																supervisor_released=False,
																deleted=False)

	#Create a list with meetings in it.
	meetings_list = []

	"""
	" Get the next meeting.
	"""
	nextm = get_next_meeting()


	if nextm and (nextm.startdate.month != month or nextm.startdate.year != year):

		print str(nextm.startdate.month)+":"+str(nextm.startdate.year)
		print str(month)+":"+str(year)

		nextmeeting = {
			'next_view_meeting':view_meeting(request,nextm),
			'next_edit_meeting_form1':edit_meeting_form1(request,nextm),
			'next_edit_meeting_form2':edit_meeting_form2(request,topics,nextm),
		}

	else:

		nextmeeting = None

	#Loop through each meeting on the calendar.
	for m in meetings:

		meeting_dict = {}

		"""
		" This loads the meeting view, when you click on a calendar
		"		item this is the modal that gets loaded.
		"""
		view_meeting_var = view_meeting(request,m)
		"""
		" Load the edit meeting information form.
		"""
		edit_meeting_form1_var = edit_meeting_form1(request, m)
		"""
		" Load the meeting schedule editor.
		"""
		edit_meeting_form2_var = edit_meeting_form2(request,topics,m)

		#Merge to the meeting context variable.
		meeting_dict['view_meeting'] = view_meeting_var
		#Merge to the meeting context variable.
		meeting_dict['edit_meeting_form1'] = edit_meeting_form1_var
		#Load the edit meeting dict.
		meeting_dict['edit_meeting_form2'] = edit_meeting_form2_var


		#Add the meetings to the list.
		meetings_list.append(meeting_dict)

	"""
	" End of getting the views for each meeting.
	"""


	"""
	" Get the form for adding a meeting to the form.
	"""

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
										AddMeetingForm(
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
	"""
	" End of getting the form for adding a meeting.
	"""



	"""
	" Create the calendar object.
	"""
	#Get the calendar.
	calendar = mark_safe(MeetingCalendar(meetings).formatmonth(year, month))
	"""
	" End of calendar object.
	"""

	context = {
		
		'title':'Meetings',
		'meetings_list':meetings_list,
		'meetingform':meetingform,
		'calendar': calendar,
		'nextmeeting':nextmeeting,
		
		###
		# These are the month variables.
		###
			
			#The previous month in the year.
			'prev_month':prev_month,
			#The next month in the year.
			'next_month':next_month,
			#This is a textual version of the previous month.
			'prev_month_textual':prev_month.strftime("%b, %Y"),
			#This is a textual version of the next month.
			'next_month_textual':next_month.strftime("%b, %Y"),
		
		###
		# End of the month variables.
		###

		#If the modal needs to be loaded
		'loadform':loadform

	}



	#Render the request information.
	return render(request,
 			'meeting_management/viewmeetings.html',
			context)

# Create your views here.
@login_required
def oldviewmeetings(request):

	#Update the meeting information, this updates just this information:
	#		-The name.
	#		-The description.
	#		-The start time.
	if 'update_meeting_information' in request.POST:
		
		#Update this publicid
		publicid = request.POST['update_meeting_information']

		#Get the meeting to edit.
		meeting_to_edit = Meeting.objects.get(publicid=publicid)
		
		#Update the meeting name.
		meeting_to_edit.name = request.POST['name']
		#Update the meeting description.
		meeting_to_edit.description = request.POST['description']
		#Update the meeting start time.
		meeting_to_edit.starttime =format_time(request.POST['starttime'])

		#Save the meeting.
		meeting_to_edit.save()

		return redirect('/viewmeetings/#%s'%publicid)

	#Update the meeting schedule order, the order is the right way.
	if 'update_meeting_schedule_publicid' in request.POST:
		
		#Update this publicid
		publicid = request.POST['update_meeting_schedule_publicid']

		#Get the meeting to edit.
		meeting_to_edit = Meeting.objects.get(publicid=publicid)

		#Get the schedule_items.
		schedule_items = request.POST['schedule_items'].split(',')
		#Update the meeting schedule.
		update_meeting_schedule(meeting_to_edit,schedule_items,new=False)
		#Update the items on the schedule.
		meeting_to_edit.maxscheduleitems = len(schedule_items)
		#Save the meeting information.
		meeting_to_edit.save()

		return redirect('/viewmeetings/#%s'%publicid)


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
											{
												'meeting':m,
												'topics':m.topics.order_by('scheduleorder')
											}
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
									extra_fields='<input type="hidden" name="update_meeting_information" value="%s"/>' % m.publicid,
									#Add a special form action
									action="%s#%s"% (request.get_full_path(),m.publicid)
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
 			'meeting_management/oldviewmeetings.html',
			context)