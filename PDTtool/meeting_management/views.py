from datetime import date
from PDTtool import settings
from django.utils import timezone
from datetime import timedelta, datetime
from topic_management.models import Topic
from django.utils.safestring import mark_safe
from meeting_management.models import Meeting
from dateutil.relativedelta import relativedelta
from meeting_management.forms import AddMeetingForm
from djnotifications import lib as notificationslib
from schedule_management.models import CategorySchedule
from pdtresources.MeetingsCalendar import MeetingCalendar
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from schedule_management import resources as scheduleresources
from meeting_management.notifications import meeting_notification
from meeting_management import notifications as meeting_notifications
from meeting_management.resources import  IsSupervisor, meeting_url_string
from meeting_management.resources import format_time, format_date, update_meeting_schedule

def create_meeting_notification(date_of_event=timezone.now(),
																user=None,
																subject=None,
																template_name = None,
																meeting_pk=None,
																notification_set=None,
																modulename=None,
																task=None,
																message="Notify the user of a meeting event."
																):

	day_increments = (7,3,2,1)
	time_right_now = timezone.now().date()

	if (not user or
			not template_name or
			not meeting_pk or
			not notification_set or
			not modulename or
		  not task):
		return False

	if date_of_event is str or isinstance(date_of_event,unicode):
		date_of_event = datetime.strptime(date_of_event, "%Y-%m-%d").date()

	for i in range(4):
		day_count = day_increments[i]
		notification_time = date_of_event - timedelta(days=day_count)
		if notification_time >= time_right_now:

			message = "%s | day %d" % (message, day_count)

			notificationslib.create_notification(
				modulename=modulename,
				task=task,
				message=message,
				user=user,
				time_of_notification=notification_time,
				arguments={
					'meeting_pk':meeting_pk,
					'day_count':day_count,
					'template_name':template_name,
					'notification_set':notification_set,
					'notification_day_count':day_count,
					'subject':subject
				}
			)

def testing(request):

	return HttpResponse("Gotta test!!")

###################################################
# view viewmeetings: This is the view where user 
#							can view the meetings. A Supervisor
#          		can manage all of the meetings in
#							this view.
@login_required
def viewmeetings(request):

	"""
	" Generate the handlers for all of the data.
	"""
	#Check if the user is a supervisor.
	if IsSupervisor(request):

		"""
		" Handle the deletion of a meeting.
		"""
		#Update the meeting information, this updates just this information:
		#		-The name.
		#		-The description.
		#		-The start time.
		if 'delete_meeting' in request.POST:
			#Update this publicid
			publicid = request.POST['delete_meeting']
			#Get the meeting to edit.
			meeting_to_delete = Meeting.objects.get(publicid=publicid)
			#Get the name of the meeting.
			name = meeting_to_delete.name

			#Delete the meeting schedule.
			scheduleresources.delete_meeting_schedule(meeting=meeting_to_delete)
			
			#Get the url string to redirect to.
			redirect_url_string = meeting_url_string(meeting_to_delete.publicid,(('deleted',name),))

			#Save the meeting.
			meeting_to_delete.delete()

			#Clear any notifications that the meeting might have.
			notificationslib.clear_notifications(task_argument_keyword='meeting_pk',task_argument_value=meeting_to_delete.pk)

			#Redirect to the meetings.
			return redirect(redirect_url_string)

		"""
		" End the handle of updating meeting information.
		"""

		#Add a meeting to the calendar, or edit a meeting already on the calendar.
		if 'add_meeting' in request.POST or 'edit_meeting' in request.POST:
			#Get the category order for all of the topics.
			schedule_categories = request.POST['schedule_categories'].split(',')
			#Get the publicid for all of the topics.
			schedule_items = request.POST['schedule_items'].split(',')
			#Format the duedate.
			duedate = format_date(request.POST['duedate'])
			#Format the startdate.
			startdate =  format_date(request.POST['startdate'])
			#Get the starttime.
			starttime = format_time(request.POST['starttime'])
			#Get the name of the meeting.
			meeting_name = request.POST['name']
			#Get the description of the meeting.
			meeting_description = request.POST['description']
			#Get the description of the meeting, we convert it from hours to minutes.
			meeting_duration = int(request.POST['duration']) * 60 if request.POST['duration'] else 0



			# If there is a meeting being added.
			if 'add_meeting' in request.POST:
				#Define the action we are taking
				action = "added"
				#Define a new meeting
				meeting = Meeting(
													name = meeting_name,#Set the meeting name.
													description=meeting_description,#Set the meeting description.
													duedate=duedate,#Set the meeting duedate (cut off date).
													startdate=startdate,#Set the meeting startdate.
													starttime=starttime,#Set the meeting starttime.
													maxscheduleitems=len(schedule_items),#Set the max scheduleitems.
													user=request.user,#Set the user request.
													duration=meeting_duration#Set the duration of the meeting.
				)
				#This a new meeting.
				new_meeting = True

			else:#If a meeting is being updated.
				#Define the action we are taking.
				action = "updated"
				#Get the meeting public id that is being updated.
				meeting_publicid = request.POST['edit_meeting']
				#Load the Meeting objectthat is being edited from 
				meeting = Meeting.objects.get(publicid=meeting_publicid)
				#Set the meeting name to the POSt data passed.
				meeting.name = meeting_name
				#Set the meeting description to the POST data passed.
				meeting.description = meeting_description
				#Set the meeting dudate to the POST data passed.
				meeting.duedate = duedate
				#Set the meeting startdate to the POST data passed.
				meeting.startdate = startdate
				#Set the meeting start time to the POST data passed.
				meeting.starttime = starttime
				#Set the meeting max scheduled items to the amount of
				#			items the user scheduled.
				meeting.maxscheduleitems = len(schedule_items)
				#Add the meeting user to the user that is currently
				#		logged in.
				meeting.user = request.user
				#Set the meeting duration to 0, it will be set in
				#		update_meetinle a few lines down if
				#		there have been items scheduled.
				meeting.duration = meeting_duration
				#This is not a new meeting.
				new_meeting = False

			#Save the new meeting.
			meeting.save()

			#if new_meeting:

			if not new_meeting:

				notificationslib.clear_notifications(
					task_argument_keyword = 'meeting_pk',
					task_argument_value = meeting.pk
				)

			cut_off_message = "Notify the program managers of an upcoming cut off date for '%s' on %s at %s" % (
																					meeting.name,
																					meeting.startdate,
																					meeting.starttime)

			new_email_message = "Notify the attendees of an upcoming meeting date for '%s' on %s at %s" % (
																					meeting.name,
																					meeting.startdate,
																					meeting.starttime)

			subject = "A cut off date for '%s' is coming up" % (meeting.name)

			#Create the notification for the user for the count down.
			create_meeting_notification(
														date_of_event=meeting.duedate,
														user=request.user,
														subject=subject,
														template_name='countdown_notification',
														notification_set=settings.NOTIFICATION_SETS['countdown_set']['varname'],
														meeting_pk=meeting.pk,
														modulename="meeting_management.notifications",
														task="meeting_notification",
														message=cut_off_message)

			subject = "The meeting '%s' is soon" % (meeting.name)

			#Create the notification for user for the email start.
			create_meeting_notification(
														date_of_event=meeting.startdate,
														user=request.user,
														subject=subject,
														template_name='meeting_notification',
														notification_set=settings.NOTIFICATION_SETS['startdate_set']['varname'],
														meeting_pk=meeting.pk,
														modulename="meeting_management.notifications",
														task="meeting_notification",
														message=new_email_message)

			#Add Schedule.
			#update_meeting_schedule(meeting,schedule_items,new_meeting);
			scheduleresources.save_meeting_schedule(meeting,schedule_items,schedule_categories,new_meeting)

			#if new_meeting:
				#Notify all of the users that were initially added.
				#meeting_notifications.meeting_added(meeting=meeting)

			#Redirect to the meetings .
			return redirect(meeting_url_string(meeting.publicid,((action,meeting.name),)))

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
										  deleted=False,#Select if the meeting is not deleted.
										  startdate__year=displaydate.year,#Select if the year is the current displayed year.
										  startdate__month=displaydate.month,#Select if the month is the current displayed month.
										  ).order_by('startdate','starttime')#Order by the startdate and the starttime.
	"""
	" End of the meetings that will be on the calendar.
	"""

	"""
	" For each meeting get the views asociated.
	"""
	#load the topics available, for making the schedule.
	topics = Topic.objects.filter(meeting=None,#Select topics that aren't in a meeting.
																readyforreview=True,#Select if they are flagged as ready to be reviewed.
																supervisor_released=False,#Select if the supervisor has not approved.
																deleted=False)#Select if the topic is not deleted.

	#Create a list with meetings in it.
	meetings_list = []

	#Get the actual form from the form model.
	addmeetingform = mark_safe(AddMeetingForm(
													#If there is request POST information,
													#			populate the form with it.
													request.POST if 'addmeetingform' in request.POST else None
											 ).as_table())#Output the form as a table.

	"""
	" Create the calendar object.
	"""
	#Get the calendar.
	calendar = mark_safe(MeetingCalendar(meetings).formatmonth(year, month))
	"""
	" End of calendar object.
	"""

	#Create context variables to pass
	#			to the template.
	context = {
		#Creat a title for the meetings.
		'title':'Meetings',
		#Pass in the meetings list.
		'meetings_list':meetings_list,
		#Pass in the addmeeting form.
		'addmeetingform':addmeetingform,
		#Pass in the calendar.
		'calendar': calendar,
		#Pass in the topics that can be
		#			added to a meeting.
		'topics':topics,

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

	}

	#Render the request information.
	return render(request, 'meeting_management/viewmeetings.html', context)
