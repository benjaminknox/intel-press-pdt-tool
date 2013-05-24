from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, Permission

def handle_uploaded_file(f,location):
    with open(location, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return location

#This is a snippet to create pagination objects.
def paginate(request, objects, count=10, param_name='page'):

  #This is a paginator object.
  paginator = Paginator(objects, count)

  #Try the value.
  try:
      #Check the page number.
      pagenum = int(request.GET.get('%s' % param_name, '1'))
  #Except the value.
  except ValueError: 
      #Check the pagenum.
      pagenum = 1

  try:
      #Try to generate the objects.
      result = paginator.page(pagenum)
  except (EmptyPage, InvalidPage):
      #If the page is output the last page.
      result = paginator.page(paginator.num_pages)

  #Create the query
  result.qstring = request.GET.copy()

  #Check the query string for an existing page variable.
  if result.qstring.has_key(param_name):
    #Remove it if it exists.
    del result.qstring[param_name]

  
  #Return the paginator objects.
  return result


"""
" Create User Roles (groups in django) based on the use case diagram in the share.
"   -Site Admin.
"   -Supervisor.
"   -Program Manager.
"   -Guest.
"
"I will use this function to access these user roles in the views:
"
"def not_in_student_group(user):
"    if user:
"        return user.groups.filter(name='Student').count() == 0
"    return False
"
" @user_passes_test(not_in_student_group, login_url='/')
"""
def create_groups(user):
  #Try to create groups if the database has been created.
  try:
    #Check for the supervisor group.
    Supervisor = Group.objects.filter(name__iexact="Supervisor")
    if not Supervisor:
      #Create the Supervisor group.
      Supervisor = Group(name = "Supervisor")
      Supervisor.save()
      print "Creating Supervisor group."
    else:
      Supervisor = Supervisor.all()[0]
      #We have already created the supervisor group.
      print "Supervisor group already created."

    #Check for the ProgramManager group.
    ProgramManager = Group.objects.filter(name__iexact="Program Manager")
    if not ProgramManager:
      #Create the ProgramManager group.
      ProgramManager = Group(name = "Program Manager")
      ProgramManager.save()
      print "Creating Program Manager group."
    else:
      ProgramManager = ProgramManager.all()[0]
      #We have already created the ProgramManager group.
      print "Program Manager group already created."

    #Check for the Guest group.
    Guest = Group.objects.filter(name__iexact="Guest")
    if not Guest:
      #Create the Guest group.
      Guest = Group(name = "Guest")
      Guest.save()
      print "Creating Guest group."
    else:
      Guest = Guest.all()[0]
      #We have already created the Guest group.
      print "Guest group already created."

    user.groups.add(Supervisor,ProgramManager)

  except:
    print "Issue with group install, try syncing the db."