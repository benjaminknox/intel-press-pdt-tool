from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import Group
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

  #Check that the response redirects to a defined urlstring.
  def checkRedirects(self,resp,urlstring='/',resp_status_code=302,target_status_code=200):
    self.assertEquals(resp.status_code, resp_status_code)
    self.assertRedirects(resp,urlstring,target_status_code=target_status_code)


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
                  groups=False):
    #Create a testuser
    testuser = User.objects.create_user(first_name='TestFirst',
                   last_name='TestLast',
                   username=username,
                   password='test',
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
