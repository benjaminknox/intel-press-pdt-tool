from django.shortcuts import redirect

# A decorator user for UserAuth views,
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
