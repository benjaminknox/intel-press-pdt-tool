from django.test import TestCase
from django.test.client import Client, RequestFactory
from user_management.models import User, ExtendedUser, ActivateUserDB
from user_management.resources import send_activation_email

#This tests the User_managementViewTestCase.
class User_managementViewTestCase(TestCase):

  def create_user(self,username):
    #Create a testuser
    testuser = User.objects.create_user(first_name='TestFirst',
                   last_name='TestLast',
                   username=username,
                   password='test',
                   email='ben.knox@cummings-inc.com')
    testuser.is_activet = True
    testuser.save()

    #Create an extended user.
    exttestuser = ExtendedUser(user=testuser,phonenumber='0000000000')
    exttestuser.save()

    return exttestuser

  #Set up the needed data
  #   for the test.
  def setUp(self):
    #Every test needs a client.
    self.client = Client()

    User.objects.all().delete()
    ExtendedUser.objects.all().delete()

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
    self.view_test('/register/','user_management/registre.html')

  #Test the activation.
  def test_activate(self):

    #Send a user through the registration.
    resp = self.client.post('/register/',
      {
        'first_name' : 'create_user_registration_first',
        'last_name' : 'create_user_registration_last',
        'username' : 'create_user_registration_username',
        'phonenumber' : '(480)123-1245',
        'password' : 'testpassword',
        'confirm_password' : 'testpassword',
        'email' : 'bknox.contact@gmail.com'
      }
    )

    self.assertEquals(resp.status_code, 200)

    #Send a get request to the activation form.


    #Run a check on the view.
    #self.view_test('/activate/','user_management/activate.html')

    #self.view_test('/')

    #resp = self.client.get('/activate/')
   # self.assertEqual(resp.status_code,200)
  '''
  #The logout view displays login after logging out
  #   a user.
  def test_logout(self):
    """
    resp = self.client.get('/logout/')
    self.assertEqual(resp.status_code,302)
    self.assertRedirects(resp,)
    """
    pass

  ''
  def test_forgotpassword(self):
    resp = self.client.get('/forgotpassword/')
    self.assertEqual(resp.status_code,200) 

  def test_accountsettings(self):
    resp = self.client.get('/accountsettings/')
    self.assertEqual(resp.status_code,200) 

  def test_resetpassword(self):
    resp = self.client.get('/resetpassword/')
    self.assertEqual(resp.status_code,200) 

  def test_viewuseres(self):
    resp = self.client.get('/resetpassword/')
    self.assertEqual(resp.status_code,200) 
  '''