from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def viewmeetings(request):

	context = {
		'title':'This is the title.',
	}

	return render(request,
 			'meeting_management/viewmeetings.html',
			context)