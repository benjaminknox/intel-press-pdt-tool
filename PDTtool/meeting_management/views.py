#from datetime import date, timedelta
from datetime import date
from django.db.models import Q
from django.shortcuts import render, redirect
from topic_management.models import Topic
from django.utils.safestring import mark_safe
from meeting_management.models import Meeting
from dateutil.relativedelta import relativedelta 
from pdtresources.templates import output_form_as_table
#from django.views.generic.dates import MonthArchiveView
from pdtresources.MeetingsCalendar import MeetingCalendar
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test
from meeting_management.forms import MeetingForm, MeetingFormStepOne, MeetingFormStepTwo


# Create your views here.
@login_required
def viewmeetings(request):

	#Get the date of this month.
	today = date.today() + relativedelta(day=1)

	#This is the year.
	if 'year' in request.GET:
		#Get the year.
		year = request.GET['year']
	else:
		#Get the year.
		year = today.year

	year = int(year)

	#This is the month.
	if 'month' in request.GET:
		#Get the month.
		month = request.GET['month']
	else:
		#Get the month.
		month = today.month	

	month = int(month)

	#The date that will be displayed.
	displaydate = date(day=1,month=month,year=year)

	#Get the previous month
	prev_month = displaydate+relativedelta(months=-1)
	#Get the next month
	next_month = displaydate+relativedelta(months=+1)

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
	}


	#Check for POST data
	if request.method == 'POST' and 'add_meeting' in request.POST:
		#Create the meetingform
		meetingform = MeetingForm(request.POST)

		#Insert the meeting.
		if meetingform.is_valid():
			#this is the meeting.
			newmeeting = Meeting(
								#Get the name.
								name = request.POST['name'],
								#Get the description.
								description = request.POST['description'],
								#Get the duedate.
								duedate = request.POST['duedate'],
								#Get the maximum number of scheduled items.
								maxscheduleitems = request.POST['maxscheduleitems'],
								#Get the start date.
								startdate = request.POST['startdate'],
								#Get the user.
								user = request.user,
								#Get the duraction of the meetings.
								duration = request.POST['duration'],
								)
			#Save the meeting.
			newmeeting.save()
			#Clear the topics.
			newmeeting.topics.clear()
			#Loop through all the topics.
			for topicid in request.POST['topics']:
				#Get the topic from the database
				topic = Topic.objects.get(pk=topicid)
				#Save the topic to the collection.
				newmeeting.topics.add(topic)

	else:
		#Get the MeetingForm.
		meetingform = MeetingForm


	#Check to see if the user has filtered 
	#	the meetings.
	if request.method == 'POST' and False == True:
		#Get the user defined search filter
		search = request.POST['search']
		#Filter the meeting list based on the users filtered information.
		meeting_list = Meeting.objects.filter(
											  name__icontains=search,
											  startdate__year=displaydate.year,
											  startdate__month=displaydate.month,
											  deleted=False)
	else:
		#Load the meeting objects into a list
		meeting_list = Meeting.objects.filter(
											  deleted=False,
											  startdate__year=displaydate.year,
											  startdate__month=displaydate.month,
											  )
	
	#Put the meetings into a paginator object
	paginator = Paginator(meeting_list, 10) # Show 25 meetings per page
	#Get the page
	page = request.GET.get('page')

	#This block of code tries loading into a paginator object.
	try:
		#Load the meetings for this page.
		meetings = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		meetings = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		meetings = paginator.page(paginator.num_pages)

	#Get the calendar.
	cal = MeetingCalendar(meetings).formatmonth(year, month)

	#Meeting Data
	meetings = [{
			'meeting':m,
			'publicid':m.publicid,
			'meeting_view': mark_safe(
								render(
									request,
									'meeting_management/viewmeeting.html',
									{'meeting':m}
								).content
							)
		}
		for m in meetings
	]

	context['meetings'] = meetings
	context['calendar'] = mark_safe(cal)
	context['MeetingForm'] = meetingform

	return render(request,
 			'meeting_management/viewmeetings.html',
			context)

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
		context)