import os
from PDTtool import settings
from shutil import rmtree,move
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, InvalidPage

#This creates a directory for the topic.
def create_directory(topic,base_dir=settings.PROJECT_DIR,delete=True):
  #Define a directory with the topic publicid in it.
  directory = "%s/%s" % (base_dir,topic.publicid)
  #If the path already exists delete it.
  if os.path.exists(directory) and delete: rmtree(directory)
  #Make the directory
  os.makedirs(directory)
  #Return the directory
  return directory

#This handles an uploaded file.
def handle_uploaded_file(f,location):
  #This uploads a file.
  with open(location, 'wb+') as destination:
    #This is a chunk of the file.
    for chunk in f.chunks():
      #This is the destination.
      destination.write(chunk)

  return location

#Move the deleted documents to another a deleted directory
def delete_topic(topic):
  #Create a topic_publicid
  topic_publicid = topic.publicid
  #This is the uploaded topic directory.
  directory = "%s/%s"% (settings.UPLOADED_TOPIC_DIR, topic_publicid)
  #This is the deleted topic directory.
  deldirectory = "%s/%s"% (settings.DELETED_TOPIC_DIR, topic_publicid)

  #If this is the path that exists.
  if os.path.exists(directory):
    #Move the directory.
    move(directory,deldirectory)

#Delete the directory where the uploads for a topic are.
def permantently_delete_topic(topic):
  #Set a string in the directory.
  directory = "%s/%s"% (settings.DELETED_TOPIC_DIR, topic.publicid)
  #If the path exists.
  if os.path.exists(directory):
    #Remove the directory.
    rmtree(directory)

"""
" This creates a pagination object based on 
"   some object passed in.
"""
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