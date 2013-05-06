from django.shortcuts import render, redirect
from dashboard.models import Comment
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

class MeetingCalendar(HTMLCalendar):

    def __init__(self, meetings):
        super(MeetingCalendar, self).__init__()
        self.meetings = self.group_by_day(meetings)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.meetings:
                cssclass += ' filled'
                body = ['<ul>']
                for meeting in self.meetings[day]:
                    body.append('<li>')
                    body.append('<a href="#">')
                    body.append(esc(meeting.name))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(MeetingCalendar, self).formatmonth(year, month)

    def group_by_day(self, meetings):
        field = lambda meeting: meeting.start_date.day
        return dict(
            [(day, list(items)) for day, items in groupby(meetings, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

#A decorator user for UserAuth views,
#	it checks to see if the user is authenticated. 
#	It is utilized by the views, it requires:
#		-request: The http request information.
def user_is_authenticated_decorator(fn):
	def wrappedFunction(*args, **kw):
		#Get the request
		request = args[0];
		#Check if the user is authenticated.
		if request.user.is_authenticated():
			return redirect('/')
		#Return wrapped function
		return fn(*args, **kw)
	#Run the wrapped function
	return wrappedFunction

def handle_uploaded_file(f,location):
    with open(location, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return location

#We can expect document, file, and comment for comment_relationship_type
def comment_form(request, comment_relation_type = 'document', comment_relation_id=None):

	parent_id = str(comment_relation_id)
	name = comment_relation_type+'id'
	form_div_id = '%s_comment_form_%s' % (comment_relation_type, parent_id)

	content = ''

	if comment_relation_type == 'document':
		content+= '<a href="javascript:void(0);" onclick="$(\'#%s\').toggle();">Add Feedback</a>'%form_div_id

	content+= '<div id="%s" class="comment_form">'% form_div_id
	content+= 	'<form action="%s" method="POST">'% request.path
	content+= 		'<input type="hidden" name="csrfmiddlewaretoken" value="%s" />'% request.COOKIES['csrftoken']
	content+=		'<input type="hidden" name="%s" value="%s" />'% (name, parent_id,)
	content+=		'<input type="text" name="title" /><br>'
	content+=		'<textarea name="content"></textarea><br>'
	content+=		'<button type="submit" class="btn btn-primary">Go</button>'
	content+=	'</form>'
	content+= 	'<div class="clear-fix"></div>'
	content+= '</div><!-- #%s -->'% form_div_id

	return content

#TODO: escape user data.
def recursive_comments(request, parentcommentid, top_comment=True):

	parentcomment = Comment.objects.get(id=parentcommentid)
	
	if not top_comment:
		commentclass = 'child_comment'
	else:
		commentclass = 'highest_parent_comment'

	content = '<div class="comment_content">'
	content+=	'<h6>'+parentcomment.user.first_name+' '+parentcomment.user.last_name+' says:</h6>'
	content+=	'<div class="comment_body">'
	content+= 		parentcomment.content
	content+=	'</div>'
	content+=	'<a href="javascript:void(0)" class="btn btn-small reply_button" style="margin-top: -4px;" onclick="$(\'#comment_comment_form_%d\').toggle();">reply</a>'% parentcomment.id
	content+= 	'<div class="clear-fix"></div>'
	content+= '</div>'

	content += comment_form(request,'comment',parentcomment.id)

	childcomments = parentcomment.comments

	if childcomments.count() > 0:

		for childcomment in childcomments.all():

			content += recursive_comments(request,childcomment.id,False)

	return '<div class="comment_content_wrapper '+commentclass+' pull-right">'+content+'<div class="clear-fix"></div></div>'