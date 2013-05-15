#from datetime import date, timedelta
from django.shortcuts import render
from meeting_management.models import Meeting
from meeting_management.forms import MeetingForm
from topic_management.models import Topic
from pdtresources.MeetingsCalendar import MeetingCalendar
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def viewmeetings(request):

	context = {
		'title':'This is the title.',
	}


	#Check for POST data
	if request.method == 'POST' and 'add_meeting' in request.POST:
		#Create the meetingform
		meetingform = MeetingForm(request.POST)

		#Insert the meeting.
		if meetingform.is_valid():
			newmeeting = Meeting(
								name = request.POST['name'],
								description = request.POST['description'],
								duedate = request.POST['duedate'],
								maxscheduleitems = request.POST['maxscheduleitems'],
								startdate = request.POST['startdate'],
								user = request.user,
								duration = request.POST['duration'],
								)

			newmeeting.save()

			newmeeting.topics.clear()

			for topicid in request.POST['topics']:
				topic = Topic.objects.get(pk=topicid)
				newmeeting.topics.add(topic)

	else:
		meetingform = MeetingForm


	#Check to see if the user has filtered 
	#	the meetings.
	if request.method == 'POST' and False == True:
		#Get the user defined search filter
		search = request.POST['search']
		#Filter the meeting list based on the users filtered information.
		meeting_list = Meeting.objects.filter(name__icontains=search,deleted=False)
	else:
		#Load the meeting objects into a list
		meeting_list = Meeting.objects.filter(deleted=False)
	
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

	#This is the year
	year = 2013
	#This is the month
	month = 5

	#Get the calendar.
	cal = MeetingCalendar(meetings).formatmonth(year, month)

	#Edit Meeting Forms
	meetings = [{
			'meeting':m,
			'publicid':m.publicid,
			'meetingform':MeetingForm({
				'name':m.name,
				'topics':[t.id for t in m.topics.all()],
				'description':m.description,
				'duration':m.duration,
				'maxscheduleitems':m.maxscheduleitems,
				'duedate':m.duedate,
				'startdate':m.startdate,
				})
		}
		for m in meetings
	]

	context['calendar'] = cal
	context['MeetingForm'] = meetingform
	context['meetings'] = meetings

	return render(request,
 			'meeting_management/viewmeetings.html',
			context)

