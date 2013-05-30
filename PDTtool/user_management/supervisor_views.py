from django.db.models import Q
from django.shortcuts import render
from user_management.models import ExtendedUser
from django.contrib.auth.models import User, Group
from user_management.forms import UserManagementForm
from pdtresources.handles import paginate
from pdtresources.templates import form_modal
from django.contrib.auth.decorators import login_required, user_passes_test
from user_management.resources import check_existing_user, check_user_groups

###
# This allows for editing the user.
###
@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='Supervisor')).count() != 0)
def viewusers(request):
	
	context= {
			'title':'View Users',
	}

	existingusernotification = False

	#Check to see if a user has been edited
	if request.method == 'POST' and ('edit_user' in request.POST or 'add_user' in request.POST):
		"""
		" Get the form data.
		"""
		#Get the username
		newusername = request.POST['username']
		#Get the first name
		newfirst_name = request.POST['first_name']
		#Get the last name
		newlast_name = request.POST['last_name']
		#Get the email
		newemail = request.POST['email']
		#Get the phone number
		newphonenumber = request.POST['phonenumber']
		#Get the password.
		newpassword = request.POST['password']
		#Get wether or not they are active.
		is_active = False
		if 'is_active' in request.POST:
			is_active = True

		is_program_manager = False
		if 'is_program_manager' in request.POST:
			is_program_manager = True

		if 'edit_user' in request.POST:
			#Get the public id
			publicid = request.POST['edit_user']
			#Get the extended user
			extendeduser = ExtendedUser.objects.get(publicid=publicid)
		else:
			extendeduser = False

		"""
		" End the form data.
		"""

		"""
		" Check if is existing user.
		"""
		if not check_existing_user(newusername) or extendeduser and extendeduser.user.username == newusername:

			"""
			" Save the user information.

			"""
			#We are making a new user
			if extendeduser:
				#Get the username.
				extendeduser.user.username = newusername
				#Get the first name.
				extendeduser.user.first_name= newfirst_name
				#Get the last name.
				extendeduser.user.last_name = newlast_name
				#Get the email.
				extendeduser.user.email = newemail
				#Add the phonenumber
				extendeduser.phonenumber = newphonenumber
			else:
				#Create a new user
				user = User.objects.create_user(
					username=newusername,
					password=newpassword,
					first_name=newfirst_name,
					last_name=newlast_name,
					email=newemail,
				)

				extendeduser = ExtendedUser(user=user,phonenumber=newphonenumber)
			
			#Get the active boolean.
			extendeduser.user.is_active= is_active

			#Save the user.
			extendeduser.user.save()
			extendeduser.save()

			if is_program_manager:
				program_manager = Group.objects.get(name='Program Manager')
				extendeduser.user.groups.add(program_manager)
			elif check_user_groups(extendeduser.user,'Program Manager'):
				program_manager = extendeduser.user.groups.get(name='Program Manager')
				extendeduser.user.groups.remove(program_manager)

			if len(newpassword) > 0:
				extendeduser.user.set_password(newpassword)

			"""
			" End of saving the user information.
			"""
		else:
			try:
				existingusernotification = publicid
			except:
				existingusernotification = True

		"""
		" End check of existing users.
		"""
	"""
	" Filter the topics.
	"""
	#Check to see if the user has filtered 
	#	the topics.
	if request.method == 'GET' and 'search' in request.GET:
		#Get the user defined search filter
		search = request.GET['search']
		#Filter the topic list based on the users filtered information.
		users_list = ExtendedUser.objects.filter(
			~Q(user__is_superuser=True) & 
				(Q(user__username__icontains=search) | 
				 Q(user__first_name__icontains=search) |
				 Q(user__last_name__icontains=search) 
			 	)
			)
	else:
		#Load the topic objects into a list
		users_list = ExtendedUser.objects.exclude(user__is_superuser=True)


	users_object = paginate(request,users_list)

	"""
	" End filter of the topics.
	"""

	#Get a user 
	def returnfunc(request,u):

		if request.POST and 'edit_user' in request.POST and request.POST['edit_user'] == u.publicid:
			return request.POST
		else:
			return {
				'first_name':u.user.first_name,
				'last_name':u.user.last_name,
				'email':u.user.email,
				'phonenumber':u.phonenumber,
				'username':u.user.username,
				'is_active':u.user.is_active,
				'is_program_manager' : check_user_groups(u.user,'Program Manager'),
			}

	users = [{
		'publicid':u.publicid,
		'extendeduser':u,
		'user':u.user,
		'user_form':form_modal(request,
													'edit_user',
													UserManagementForm(returnfunc(request, u)).as_table(),
													modal_title = 'Edit %s'% u.user.get_full_name(),
													modal_id = 'edit_user_%s'% u.publicid,
													table_class = 'edit_user_form ',
													formname_value=u.publicid),
		'is_program_manager' : check_user_groups(u.user,'Program Manager'),
	}
	for u in users_object
	]

	#Create a user modal
	add_user_form = form_modal(request,
														'add_user',
														UserManagementForm(request.POST if 'edit_user' in request.POST else None).as_table(),
														modal_title='Add a User',
														modal_id='add_user')

	#Pass in the users.
	context['users'] = users
	context['paginated_users'] = users_object
	context['add_user_form'] = add_user_form
	context['existingusernotification'] = existingusernotification
	context['queries'] = users_object.qstring

	return render(request,
		'user_management/viewusers.html',
		context)