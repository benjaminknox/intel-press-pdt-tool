from django.db.models import get_app, get_models

###
#
# This is a template context processor.
#
# It gets the models from the dashboard app
#	and outputs the names of the class into
#	a context processor.
#
# It gets loaded in TEMPLATE_CONTEXT_PROCESSORS
#	in the settings file.
###
def dashboard_models(*args, **kw):
	
	#Load the classes from the dashboard model.
	model_classes = get_models(app_mod=get_app('dashboard'))

	#Define a dictionary to place
	#	the class names.
	dashboard_models = {}

	#Loop through the classes.
	for _class in model_classes:
		#Get the class names.
		classname = _class.__name__
		#Leave out some of the objects.
		if classname not in ('Extendeduser','File'): 
			#Load the dashboard class model
			dashboard_models[classname] = _class
	###
	# Return the dictionary to the context_processor
	#	which can be referenced as dashboard_models
	#	in the templates.
	###
	return { 'dashboard_models' : dashboard_models }

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
def search_form(request):

	#Get the CSRF token from the request cookie
	token = request.COOKIES['csrftoken']

	#Get the request path
	request_full_path = request.path

	#Output the from HTML
	html = 	'<div id="search_form">'
	html+= 		'<div class="pull-right">'
	html+= 			'<form action="%s" class="form-inline" method="post">' % request_full_path
	html+= 				'<input type="hidden" name="csrfmiddlewaretoken" value="%s">' % token
	html+= 				'<input type="text" class="datepicker" name="date" style="width: 100px" placeholder="date" />'
	html+= 				'<input type="text" name="search" class="input-medium search-query" />'
	html+= 				'<button type="submit" class="btn">Go</button>'
	html+= 			'</form><!-- (bootstrap) .form-inline -->'
	html+= 		'</div><!-- (bootstrap) .pull-right -->'
	html+= 		'<div class="clearfix"></div>'
	html+= 	'</div><!-- #search_form -->'

	#Return the variable into the context.
	return {'search_form':html}