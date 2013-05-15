from datetime import date, timedelta
from django.shortcuts import render
from meeting_management.models import Meeting
from pdtresources.MeetingsCalendar import MeetingCalendar
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def viewmeetings(request):

	context = {
		'title':'This is the title.',
	}

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
	month = 12

	day = 01

	thedate = date(year, month, day)

#	nextdate = date(year, month + 1, day)

#	print nextdate

	#Get the calendar.
	cal = MeetingCalendar(meetings).formatmonth(year, month)

	context['calendar'] = cal

	return render(request,
 			'meeting_management/viewmeetings.html',
			context)

