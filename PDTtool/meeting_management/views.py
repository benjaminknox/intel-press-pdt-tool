from datetime import date
from time import strptime,strftime
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


# Create your views here.
@login_required
def viewmeetings(request):
	
	#Check for a meeting.
	if 'schedule_items' in request.POST and 'addmeetingform' in request.session:
		#Add the meeting form a session variable.
		form = request.session['addmeetingform']
		#Get the publicid for all of the topics.
		schedule_items = request.POST['schedule_items'].split(',')
		#Format the date properly, this takes the month variables
		#		and adds a 0 if it is one character long.
		format_date = lambda t: '0'+ t if len(t) == 1 else t
		#Format the duedate.
		duedate = '/'.join([format_date(t) for t in form['duedate'].split('/')])
		#Format the duedate into django format for a string.
		duedate = "%s-%s-%s"%(duedate[6:],duedate[0:2],duedate[3:5])
		#Format the startdate.
		startdate = '/'.join([format_date(t) for t in form['startdate'].split('/')])
		#Format the startdate into django format for a string.
		startdate = "%s-%s-%s"%(startdate[6:],startdate[0:2],startdate[3:5])
		#Get the starttime
		starttime = strftime('%I:%M:%S',strptime(('0'+form['starttime'] if len(form['starttime']) == 6 
														else form['starttime']).upper(),
													'%I:%M%p'))
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
		#Increment a variable.
		i = 0
		#Add an integer for the duration.
		duration = 0
		#Loop through the itemes.
		for publicid in schedule_items:
			#Increment the count.
			i += 1
			#Check to make sure the publicid is not null.
			if publicid:
				#Get the topic based on the publicid.
				topic = Topic.objects.get(publicid=publicid)
				#Get the topic schedule order.
				topic.scheduleorder = i
				#Add the meeting to the topic.
				topic.meeting = newmeeting
				#Save the topic.
				topic.save()
				#Add the topic to the meeting.
				newmeeting.topics.add(topic)
				#Add the duration to the meeting.
				duration += topic.presentationlength
		#Add a new meeting in the duration.
		newmeeting.duration = duration
		#Save the meeting.
		newmeeting.save()

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
									modal_id=m.publicid
								).content
							),
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
									modal_id='editmeetingform1_%s' % m.publicid
								),
				'edit_meeting_form2':mark_safe(
						#Load a modal template 
						modal(
								request,
								mark_safe(render(request,
													'meeting_management/addmeetingform2.html',
													{
														'topics':topics,
														'topics_schedule':m.topics
													}).content
										),
								modal_title='Create a Schedule',
								modal_id='editmeetingform_%s' % m.publicid
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
				modal(
						request,
						addmeetingform2,
						modal_title='Create a Schedule',
						modal_id='addmeetingform'
				).content
			)

		loadform = True
	
	else:

		loadform = True if 'loadprevious' in request.GET else False

		if not loadform and 'addmeetingform' in request.session:
			del request.session['addmeetingform']

		#Get the first meeting form
		meetingform = form_modal(request,
										#Add the meeting form.
										'addmeetingform',
										#Get the actual form from the form model.
										MeetingFormStepOne(
												request.POST if 'addmeetingform' in request.POST else 
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

	return render(request,
 			'meeting_management/viewmeetings.html',
			context)



"""
@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='Supervisor')).count() != 0)
def addmeeting(request):

	if 'step' in request.GET and int(request.GET['step']) == 2 and request.POST:
		request.session['form1'] = request.POST
		meetingform = MeetingFormStepTwo()
		step = "Two"
		nextstepquerystring = ""
		name = 'meeting_form2'

	else:

		if 'form1' in request.session:
			meetingform = MeetingFormStepOne(request.session['form1'])
		else:
			meetingform = MeetingFormStepOne()

		step = "One"
		name = 'meeting_form1'
		nextstepquerystring = "&step=2"

	#Save the meeting.
	if 'meeting_form2' in request.POST and 'form1' in request.session:

		form1 = request.session['form1']
		form2 = request.POST

		for key,value in request.POST.lists():
			if key == 'topics':
				selected_topics = value

		newmeeting = Meeting(
						name=form1['name'],
						description=form1['description'],
						maxscheduleitems=form1['maxscheduleitems'],
						duedate=form1['duedate'],
						startdate=form1['startdate'],
						duration=form2['duration'],
						user=request.user,
					)

		newmeeting.save()

		for topicid in selected_topics:
			topic = Topic.objects.get(pk=topicid)
			newmeeting.topics.add(topic)

		return redirect('/viewmeetings/#%s'%newmeeting.publicid)
 
	meetingform = output_form_as_table(
										request,
										name,
										meetingform.as_table(),
										table_class='form-table',
										get_string=nextstepquerystring,
										)

	context= {
			'title':'Meeting Form Step %s' % step,
			'MeetingForm':mark_safe(meetingform),
	}

	return render(request,
		'meeting_management/addmeeting.html',
		context)"""