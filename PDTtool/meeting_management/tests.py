from pdtresources.testsimplifier import Client,Testsimplifier
from meeting_management.models import Meeting


# Create your tests here.
class Meeting_managementViewsTestCase(Testsimplifier):

  def test_viewmeetings(self):

    url = '/viewmeetings/'
    template = 'meeting_management/oldviewmeetings.html'
    #Define a variable for the password.
    password='test'

    #Load a client
    C = Client()
    
    #Load /viewmeetings/, the response should redrect
    #   to /login/ because the user has not logged in.
    resp = C.get(url)
    #Test if there is a location to redirect to.
    self.assertIn('Location',resp)
    #Check that the location is to a login screen.
    self.assertIn('/login/',resp['Location'])



    #Create a guest user
    username = 'test.guest'
    self.create_user(username,password=password)

    #Login to the client
    C.login(username=username,password=password)

    #Load /viewmeetings/, the response should not contain an
    #   user interface because we are not a Supervisor.
    resp = C.get(url)
    #Test if the add document form is present in the page,
    #   if it is not the check passes.
    self.assertNotContains(resp,'function add_meeting_modal(date_clicked)')

    #Log the user out.
    C.logout()


    #Create a 'Program Manager' user
    username = 'test.pm'
    self.create_user(username,password=password,groups=('Program Manager',))

    #Login the user.
    C.login(username=username,password=password)

    #Load /viewmeetings/, the response should not contain an
    #   user interface because we are not a Supervisor.
    resp = C.get(url)
    #Test if the add document form is present in the page,
    #   if it is not the check passes.
    self.assertNotContains(resp,'function add_meeting_modal(date_clicked)')

    #Log the user out.
    C.logout()



    #Create a 'Supervisor' user
    username = 'test.supervisor'
    self.create_user(username,password=password,groups=('Program Manager','Supervisor'))

    #Login the user.
    C.login(username=username,password=password)

    #Load /viewmeetings/, the response should contain a
    #   user interface because we are a supervisor
    resp = C.get(url)

    #Test if the add document form is present in the page,
    #   if it is the check will pass.
    self.assertContains(resp,'function add_meeting_modal(date_clicked)')


    meeting_name = 'XIBNFELUQKO'

    #Generate post data for the first meeting form.
    postData = {
      'addmeetingform':'1',
      'name':meeting_name,
      'description':'Test Meeting Description',
      'duedate':'2013-05-05',
      'startdate':'2013-05-06',
      'starttime':'2:00am',
    }
    #Load /viewmeetings/, test that the posting of the 
    #   meeting form works.
    resp = C.post("%s?loadnext" % url,postData)


    #Believe it or not this is a unique identifier for the 
    #  editing a schedule form. Because the meeting object
    #   has not been created it doesn't have a value after
    #   the # (hash).
    unique_identifier = '''<center>
<form action="/viewmeetings/#"'''

    #Check that the second meeting form loads when it is
    #   expected too.
    self.assertContains(resp,unique_identifier)
    
    #load 
    session = C.session
    session['addmeetingform'] = postData
    session.save()

    #Load topics into the database.
    topics = [
           self.add_topic_form(C,description=' Topic 1'),
           self.add_topic_form(C,description=' Topic 2'),
           self.add_topic_form(C,description=' Topic 3'),   
    ]
    #Create a string to send through to the 
    schedule_items = ""
    for t in topics:
      #Add the public id to the list
      schedule_items += "%s," % t.publicid

    #Add a schedule_items variable.
    postData = {'schedule_items':schedule_items}
    #Get the redirect url.
    next_url = C.post("%s?loadnext" % url, postData)['Location']
    #Load the response of the redirect url.
    resp = C.post(next_url)
    #Check that the meeting is posted out onto the page.
    self.assertContains(resp,meeting_name)

    #Load a meeting to edit.
    meeting = Meeting.objects.get(name__contains=meeting_name)
    
    #Define a meeting description string.
    meeting_description = 'KRPOUSILUEKI9081'
    meeting_publicid = meeting.publicid

    #Generate post data for the first meeting form.
    postData = {
      'update_meeting_information':meeting_publicid,
      'name':meeting_name,
      'description':meeting_description,
      'duedate':'2013-05-05',
      'startdate':'2013-05-06',
      'starttime':'2:00am',
    }

    #Get the redirect url.
    next_url = C.post(url, postData)['Location']
    #Load the redirected url.
    resp = C.post(next_url)
    #Check that the meeting information has been updated.
    self.assertContains(resp,meeting_description)

    #Create a new topic description.
    topic_description = ' XESRFNIF'
    #Append the topic to the end of the schedule list.
    newtopic = self.add_topic_form(C,description=topic_description)
    schedule_items += '%s,'%newtopic.publicid
    #Create some postData.
    postData = {
      'update_meeting_schedule_publicid':meeting_publicid,
      'schedule_items':schedule_items,
    }

    #Get the next url.
    next_url = C.post(url,postData)['Location']
    #Load the redirected url.
    resp = C.post(next_url)
    #Check that the topic has been added to the meeting list.
    self.assertContains(resp, topic_description)

    #Send post data to delete the meeting we have been working on.
    postData = {
      'delete_meeting':meeting_publicid,
    }

    #Get the next url.
    next_url = C.post(url,postData)['Location']
    #Load the redirected url.
    resp = C.post(next_url)
    #Check that the meeting has been deleted, if the meeting 
    #   has been deleted the meeting_description will not be
    #   in the page anymore.
    self.assertNotContains(resp, meeting_description)


    #Log the user out.
    C.logout()