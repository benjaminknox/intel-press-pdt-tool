from PDTtool import settings
from topic_management.models import Topic

###
#
# Create a search form to be used 
#	in all the templates.
#
# It gets loaded in the TEMPLATE_CONTEXT_PROCESSOR
#	in settings.py.
#
#	The way that this would be used in the template is
#		like this in order to disable escaping:
#
#		{{ search_form|safe }}
#
# There is no user input here so it doesn't have
#		to be escaped.
#
###
def search_form(request=None):

	#Get the CSRF token from the request cookie
	#token = request.COOKIES['csrftoken']

	#Get the request full path
	request_full_path = request.path


	value = ""
	if 'search' in request.GET:
		value = request.GET['search']

	#Output the from HTML
	html = 	'<div id="search_form">'
	html+= 		'<div class="pull-right">'
	html+= 			'<form action="%s" class="form-inline" method="GET">' % request_full_path
	html+=				'<a href="%s" class="btn btn-link pull-left">clear</a>' % request_full_path
	#html+= 				'<input type="hidden" name="csrfmiddlewaretoken" value="%s">' % token
	#html+= 				'<input type="text" class="datepicker" name="date" style="width: 100px" placeholder="date" />'
	html+= 				'<input type="text" name="search" value="%s" class="input-medium search-query" />'% value
	html+= 				'<button type="submit" class="btn">Go</button>'
	html+= 			'</form><!-- (bootstrap) .form-inline -->'
	html+= 		'</div><!-- (bootstrap) .pull-right -->'
	html+= 		'<div class="clearfix"></div>'
	html+= 	'</div><!-- #search_form -->'

	#Return the variable into the context.
	return {'search_form':html}

def get_topic_categories(request):

	#These are the categories.
	topic_cats = settings.TOPIC_CATEGORIES

	#Make a list of the topic_categories.
	topic_categories = []

	#Get the category.
	for category in topic_cats:
		#Get the topic count.
		topic_count = len(Topic.objects.filter(category=category,deleted=False).all().values_list())
		#Get the topic categories.
		topic_categories.append({
				#Get the name of the category.
				'name':category,
				'code_name':category.lower().replace(' ','-'),
				#Get the count of the category.
				'count':topic_count,
				})

	topic_categories = {
		'topic_categories':topic_categories,
	}

	return topic_categories