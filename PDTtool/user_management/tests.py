from django.test import TestCase
from django.test.client import Client
from user_management.models import User, ExtendedUser, ActivateUserDB, ForgotPasswordDB

#This tests the User_managementViewTestCase.
class User_managementViewTestCase(TestCase):

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


  def create_user(self,username,is_superuser=False):
    #Create a testuser
    testuser = User.objects.create_user(first_name='TestFirst',
                   last_name='TestLast',
                   username=username,
                   password='test',
                   email='ben.knox@cummings-inc.com')
    testuser.is_active = True
    testuser.is_superuser = is_superuser
    testuser.save()

    #Create an extended user.
    exttestuser = ExtendedUser(user=testuser,phonenumber='0000000000')
    #Save the extended user.
    exttestuser.save()

    #Return the user.
    return exttestuser

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
    self.assertEquals(resp.status_code, 200)
    self.assertTemplateUsed(resp, view)
    del resp

    ###
    # Check the response when the user is logged in.
    ###
    #Log the test user in.
    C.login(username=username,password=password)
    resp = C.get(url)
    #Check that the user has a response of 302: found.
    self.assertEqual(resp.status_code,302)

  """
  " This starts the actual test methods.
  """

  #The login view displays login, if the user is logged
  #   in it redirects to /viewmeetings/.
  def test_login(self):

    #Run a check on the view.
    self.view_test('/login/','user_management/login.html')

  def test_register(self):

    #Run a check on the view.
    self.view_test('/register/','user_management/register.html')

  #Test the activation.
  def test_activate(self):

    #Run a register form
    resp = self.register_form('test.username')

    #Check to see the registration page returned
    self.assertEquals(resp.status_code, 200)

    #Delete the resp variable.
    del resp

    #Get the user.
    user = ExtendedUser.objects.get(user__username='test.username')

    #Check the activation page.
    activate = ActivateUserDB.objects.get(user=user)

    #Send a get request to the activation form.
    resp = self.client.get('/activate/',{
      'publicid':activate.publicid,
      'userid':user.publicid
    })

    #Check to see if the right template returned.
    self.assertEquals(resp.status_code, 200)
    self.assertTemplateUsed(resp, 'user_management/activate.html')

  
  #The logout view displays login after logging out
  #   a user.
  def test_logout(self):

    #Create a new client.
    C = Client()

    #Login the test user
    C.login(username='test.user',password='test')

    #Check the the user is logged in.
    self.assertIn('_auth_user_id', C.session)

    #Get the logout screen.
    resp = C.get('/logout/')

    #Check that the status redirects properly.
    self.assertEquals(resp.status_code, 302)

    #Check the the user is no longer logged in.
    self.assertNotIn('_auth_user_id', C.session)

  def test_forgotpassword(self):

    url = '/forgotpassword/'

    ###
    # Run a check without any variables in GET or POST.
    ###
    #Load the form as just a regular get form.
    resp = self.client.get(url)

    #Test to see if the right message is in the context.
    self.assertEquals(resp.status_code, 200)
    self.assertTemplateUsed(resp,'user_management/forgotpassword.html')
    del resp

    ###
    # Run the form, creating a username and a new password.
    ###
    #This is the username
    username = 'test.username'

    #Run a register form
    resp = self.register_form(username)
    del resp

    #First test the post of the form.
    resp = self.client.post(url,{'username':username})

    #Test to see if the right message is in the context.
    self.assertEquals(resp.status_code, 200)
    self.assertTemplateUsed(resp,'user_management/forgotpasswordresetemail.html')
    del resp

    ###
    # Run a check sending get data to actually reset the password.
    ###
    #Get the user.
    user = ExtendedUser.objects.get(user__username=username)
    #Get the ForgotPassword table.
    forgotpassword = ForgotPasswordDB.objects.get(user=user)

    #Send a get request to the activation form.
    resp = self.client.get(url,{
      'publicid':forgotpassword.publicid,
      'userid':user.publicid
    })

    #Check to see if the right template returned.
    self.assertEquals(resp.status_code, 200)
    self.assertTemplateUsed(resp, 'user_management/forgotpasswordresetlink.html')    

  def test_accountsettings(self):

    C = Client()
    
    C.login(username='test.user',password='test')

    url = '/accountsettings/'

    resp = C.get(url)
    self.assertEquals(resp.status_code, 200)
    self.assertTemplateUsed(resp,'user_management/accountsettings.html')
    del resp

    postData = {
        'first_name':'testuser',
        'last_name':'testuser',
        'email':'test@example.com',
        'password':'test',
        'phonenumber':'(480)123-2223',
      }

    ###
    # Check for a bad password.
    ###
    resp = C.post(url,postData)
    
    self.assertEquals(resp.status_code, 200)
    self.assertContains(resp, 'Your information is updated.')
    del resp

    ###
    # Check for a bad password.
    ###
    postData['password'] = "BadPassword"
    resp = C.post(url,postData)

    self.assertEquals(resp.status_code, 200)
    self.assertContains(resp, 'The password you entered did not match our records.')
    del resp


  def test_resetpassword(self):
     
    url = '/resetpassword/'

    ###
    # Check 
    ###
    C = Client()
    C.login(username='test.user',password='test')

    resp = C.get(url)
    self.assertEquals(resp.status_code, 200)
    self.assertTemplateUsed(resp,'user_management/resetpassword.html')
    del resp

    postData = {
      'newpassword':'check123',
      'confirmpassword':'check123',
      'password':'BadPassword'
    }

    ###
    # Check that the user entered a bad password is working.
    ###
    resp = C.post(url,postData)
    self.assertEquals(resp.status_code, 200)
    self.assertContains(resp,'The password you entered did not match the one in our records.')

    ###
    # Check that the passwords didn't match is working.
    ###
    postData['confirmpassword'] = 'check124'
    postData['password'] = 'test'
    resp = C.post(url,postData)
    self.assertEquals(resp.status_code, 200)
    self.assertContains(resp,'The passwords you entered do not match.')

    ###
    # Check that the passwords didn't match is working.
    ###
    postData['confirmpassword'] = 'check123'
    postData['password'] = 'test'
    resp = C.post(url,postData)
    self.assertEquals(resp.status_code, 200)
    self.assertContains(resp,'Your information is updated.')

  def test_viewusers(self):

    self.create_user('test.superuser', 'test')

    

    resp = self.client.get('/resetpassword/')
    self.assertEqual(resp.status_code,200) 
