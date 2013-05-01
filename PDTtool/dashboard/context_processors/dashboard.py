from django.db.models import get_app, get_models

#This gets the models in the dashboard app
#	and outputs the names of the class into a context processor
def dashboard_models(*args, **kw):
	
	#Load the classes from the dashboard model
	model_classes = get_models(app_mod=get_app('dashboard'))

	#Define a dict to 
	#	place the class names
	dashboard_models = {}

	#Loop through the classes
	for _class in model_classes:
		#Get the class names.
		classname = _class.__name__
		#Leave out some of the objects
		if classname not in ('Extendeduser','File'): 
			dashboard_models[classname] = _class

	return { 'dashboard_models' : dashboard_models }