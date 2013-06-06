from django.test import TestCase
import PDTtool.settings as settings
from django.test.client import Client
from django.contrib.auth.models import Group
from topic_management.models import Topic, Document
from user_management.models import User, ExtendedUser

class Testsimplifier(TestCase):
  #Check the template used is the one listed.
  def checkTemplateUsed(self,resp,templatename,resp_status_code=200):
    self.assertEquals(resp.status_code, resp_status_code)
    self.assertTemplateUsed(resp,templatename)

  #Check that the response contains a string.
  def checkRespContains(self,resp,string,resp_status_code=200):
    self.assertEquals(resp.status_code, resp_status_code)
    self.assertContains(resp,string)

  #Check that the response contains a string.
  def checkRespNotContains(self,resp,string,resp_status_code=200):
    self.assertEquals(resp.status_code, resp_status_code)
    self.assertNotContains(resp,string)

  #Check that the response redirects to a defined urlstring.
  def checkRedirects(self,resp,urlstring='/',resp_status_code=302,target_status_code=200):
    self.assertEquals(resp.status_code, resp_status_code)
    self.assertRedirects(resp,urlstring,target_status_code=target_status_code)

  #Check if the user is logged in
  def checkUserLoginViews(self,url,redirect_url):

    #Check the redirect when a user is not logged in.
    resp = self.client.get(url)
    self.checkRedirects(resp, redirect_url)

    del resp

    #Check the redirect when a user is logged in without 
    #   being a program manager.
    C = Client()
    #Login a user.
    C.login(username='test.user',password='test')
    resp = C.get(url)
    self.checkRedirects(resp, redirect_url,target_status_code=302)
    #Logout the user.
    C.logout()

    del resp

  #Create a user by posting to the register form.
  def register_form(self,username):

    #Send a user through the registration.
    resp = self.client.post('/register/',
      {
        'first_name' : 'create_user_registration_first',
        'last_name' : 'create_user_registration_last',
        'username' : username,
        'phonenumber' : '(480)123-1245',
        'password' : 'testpassword',
        'confirm_password' : 'testpassword',
        'email' : 'bknox.contact@gmail.com'
      }
    )

    return resp


  def create_user(self,
                  username,
                  is_superuser=False,
                  is_active=True,
                  extenduser=True,
                  groups=False,
                  password='test'):
    #Create a testuser
    testuser = User.objects.create_user(first_name='TestFirst',
                   last_name='TestLast',
                   username=username,
                   password=password,
                   email='ben.knox@cummings-inc.com')
    testuser.is_active = is_active
    testuser.is_superuser = is_superuser
    testuser.save()

    if extenduser:
        #Create an extended user.
        exttestuser = ExtendedUser(user=testuser,phonenumber='0000000000')
        #Save the extended user.
        exttestuser.save()
        user = exttestuser
    else:
        user = testuser

    #Add in the groups, defined
    #   in a list.
    if groups:
        #Group throught the list of groups.
        for g in groups:
            try:
              group = Group.objects.get(name=g)
            except:
              #Load the group.
              group = Group(name=g)
              #Save the group.
              group.save()
            #Add the usergroup.
            testuser.groups.add(group)

    #Return the user.
    return user

  #Set up the needed data
  #   for the test.
  def setUp(self):
    #Every test needs a client.
    self.client = Client()

    #Delete all of the users.
    User.objects.all().delete()
    #Delete all of the extended users.
    ExtendedUser.objects.all().delete()

    #Run the self test.
    self.test_user = self.create_user('test.user')


  """
  " First Check: When the user is logged out this test expects the string in the `view` variable.
  " Second Check:
  "        -Logs in the test user.
  "        -When the user is logged in this test expects the string in the  `url` variable.
  """
  def view_test(self,
                url,
                view,
                C=Client(),
                username='test.user',
                password='test'):
    ###
    # Check the response when the user is not logged in.
    ###
    resp = C.get(url)
    #Check the view that gets returned.

    self.checkTemplateUsed(resp, view)

   # self.assertEquals(resp.status_code, 200)
    #self.assertTemplateUsed(resp, view)
    del resp

    ###
    # Check the response when the user is logged in.
    ###
    #Log the test user in.
    C.login(username=username,password=password)
    resp = C.get(url)
    #Check that the user has a response of 302: found.
    self.assertEqual(resp.status_code,302)

  def add_topic_form(self,C,url='/addtopic/',description=''):

    f1 = "%s/www/css/jquery.timepicker.css" % settings.BASE_DIR
    f2 = "%s/www/css/jquery.ui.timepicker.css" % settings.BASE_DIR

    with open(f1) as fp1, open(f2) as fp2:

      document_name = 'test Document upload'
      document_desc = 'testing the document upload %s' % description

      #Check the return of a valid form.
      postData = {
        'name':document_name,
        'description':document_desc,
        'category':'Outline',
        'f1':fp1,
        'f2':fp2,
      }
      resp = C.post(url,postData)
      self.assertEquals(resp.status_code, 302)
      self.assertIn('viewtopic/',resp['Location'])
      #self.checkTemplateUsed(resp,'topic_management/addtopic.html')
          
      #Return the inserted topic
      return Topic.objects.get(name = document_name,description=document_desc)
