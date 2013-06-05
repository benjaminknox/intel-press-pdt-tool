from pdtresources.testsimplifier import Testsimplifier
#from django.test import TestCase
from django.test.client import Client
from user_management.models import ExtendedUser, ActivateUserDB, ForgotPasswordDB
#from selenium import webdriver

#This tests the User_managementViewTestCase.
class User_managementViewTestCase(Testsimplifier):

  """
  " This starts the actual test methods.
  """

  def test_viewusers(self):

    url = '/viewusers/'
    redirect_url = '/login/?next=/viewusers/'

    #Check that a user that has
    #   not logged in.
    resp = self.client.get(url)
    self.checkRedirects(resp, redirect_url)

    #Check that a logged in user without
    #   supervisor priveleges redirects to /.
    C = Client()
    C.login(username='test.user',password='test')
    resp = C.get(url)
    self.checkRedirects(resp,redirect_url,target_status_code=302)
    C.logout()
    del resp

    ###
    # Check that a logged in user with
    #   supervisor priveleges outputs
    #   the right template.
    # Also test the update of data 
    #   per each user.
    ###
    username = 'test.viewusersuper'
    superuser = self.create_user(username=username,is_superuser=True,groups=('Supervisor','Program Manager'))

    C.login(username=username,password='test')

    username = 'test.viewuseradd'
    view = 'user_management/viewusers.html'

    #Get a response with post data checking to see 
    #   if it returns positively.
    postAddUserData = {
        'add_user':'1',
        'username':username,
        'first_name':'first_name',
        'last_name':'last_name',
        'email':'email@example.com',
        'phonenumber':'(000)000-0000',
        'password':'hello',
        'is_active': True,
        'is_program_manager':True,
    }

    #Test the searching method that it works properly.
    resp = (C.get(url),
            C.get(url,{'search':'Test'}),
            C.post(url,postAddUserData))

    #Loop through each respons.
    for r in resp:
        self.checkTemplateUsed(r, view)
    del resp

    #Get a response with post data editing a user.
    extendeduser = ExtendedUser.objects.get(user__username=username)
    postEditUserData = postAddUserData.copy()
    postEditUserData['edit_user'] = extendeduser.publicid
    del postEditUserData['add_user']

    resp = C.post(url,postEditUserData)
    self.checkTemplateUsed(resp, view)
    del resp

    #Check the deactivation of a program manager
    del postEditUserData['is_program_manager']
    resp = C.post(url,postEditUserData)
    self.checkTemplateUsed(resp, view)

    #Check the deactivation of a program manager
    resp = C.post(url,postAddUserData)
    self.checkRespContains(resp, 'The username you submited already exists.')

    #self.checkTemplateUsed(resp,'')

    #self.assertEquals(resp.status_code,200)
    #self.assertTemplateUsed

   # self.create_user('test.superuser', 'test') 
   #resp = self.client.get('/resetpassword/')
   # self.assertEqual(resp.status_code,200) 

  #The login view displays login, if the user is logged
  #   in it redirects to /viewmeetings/.
  def test_login(self):

    url = '/login/'

    #Run a check on the view.
    self.view_test(url,'user_management/login.html')

    #Run a test on the login form, check
    #   a bad username and password.
    postData = {
        'username':'baduser.name',
        'password':'badpassword'
    }

    resp = self.client.post(url,postData)

    self.checkRespContains(resp, "Incorrect username or password")

    del resp

    #Run a test on the login form, check
    #   an inactive user.

    username = 'testlogin.user'

    self.create_user(username,is_active=False)

    postData = {
        'username':username,
        'password':'test'
    }

    resp = self.client.post(url,postData)
    self.checkRespContains(resp, "You have not been activated, please check your email")

    del resp

    #Run a test on the login form, check
    #   an active superuser.
    url = "%s?next=/viewmeetings/" % url

    username = 'testsuperlogin.user'

    self.create_user(username,is_superuser=True, extenduser=False)

    postData = {
        'username':username,
        'password':'test'
    }

    resp = self.client.post(url,postData)
    self.checkRedirects(resp,urlstring='/viewmeetings/')

  def test_register(self):

    #Run a check on the view.
    self.view_test('/register/','user_management/register.html')

  #Test the activation.
  def test_activate(self):

    url = '/activate/'

    #Run the url
    resp = self.client.get(url)

    self.checkRedirects(resp, urlstring='/login/')

    #self.assertRedirects(resp, '/login/')

    #Delete the resp variable
    del resp

    #Run a register form
    resp = self.register_form('test.username')

    #Check to see the register was page returned
    self.checkTemplateUsed(resp,templatename='user_management/registersuccess.html')

    #Delete the resp variable.
    del resp

    #Get the user.
    user = ExtendedUser.objects.get(user__username='test.username')

    #Check the activation page.
    activate = ActivateUserDB.objects.get(user=user)

    #Send a get request to the activation form.
    resp = self.client.get(url,{
      'publicid':activate.publicid,
      'userid':user.publicid
    })

    #Check to see if the right template returned.
    self.checkTemplateUsed(resp, 'user_management/activate.html')

    #Delete the resp variable.
    del resp

    #Send a get request to the activation form.
    resp = self.client.get(url,{
      'publicid':'publicidtest',
      'userid':'publicidusertest'
    })

    #Check to see if the right template returned.
    self.checkRedirects(resp, '/login/')

    #self.assertTemplateUsed(resp, 'user_management/activate.html')
    

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
    self.checkRedirects(resp, '/login/')

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
    self.checkTemplateUsed(resp, 'user_management/forgotpassword.html')
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
    self.checkTemplateUsed(resp, 'user_management/forgotpasswordresetemail.html')
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
    self.checkTemplateUsed(resp, 'user_management/forgotpasswordresetlink.html')
    del resp

    #Send a get request to the activation form for a request that doesn't exists.
    resp = self.client.get(url,{
      'publicid':"forgotpasswordtest",
      'userid':"forgotpasswordtest"
    })
    #Check to see if the right template returned.
    self.checkTemplateUsed(resp, 'user_management/forgotpassword.html')

  def test_accountsettings(self):

    C = Client()
    C.login(username='test.user',password='test')
    url = '/accountsettings/'
    resp = C.get(url)
    self.checkTemplateUsed(resp, 'user_management/accountsettings.html')

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
    self.checkRespContains(resp,'Your information is updated.')

    #self.assertEquals(resp.status_code, 200)
   # self.assertContains(resp, 'Your information is updated.')
    del resp

    ###
    # Check for a bad password.
    ###
    postData['password'] = "BadPassword"
    resp = C.post(url,postData)
    self.checkRespContains(resp,'The password you entered did not match our records.')

    #self.assertEquals(resp.status_code, 200)
    #self.assertContains(resp, 'The password you entered did not match our records.')
    del resp


  def test_resetpassword(self):
     
    url = '/resetpassword/'

    ###
    # Check 
    ###
    C = Client()
    C.login(username='test.user',password='test')
    resp = C.get(url)
    self.checkTemplateUsed(resp, 'user_management/resetpassword.html')

    #self.assertEquals(resp.status_code, 200)
    #self.assertTemplateUsed(resp,'user_management/resetpassword.html')
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
    self.checkRespContains(resp, 'The password you entered did not match the one in our records.')

    ###
    # Check that the passwords didn't match is working.
    ###
    postData['confirmpassword'] = 'check124'
    postData['password'] = 'test'
    resp = C.post(url,postData)
    self.checkRespContains(resp, 'The passwords you entered do not match.')

    ###
    # Check that the passwords didn't match is working.
    ###
    postData['confirmpassword'] = 'check123'
    postData['password'] = 'test'
    resp = C.post(url,postData)
    self.checkRespContains(resp, 'Your information is updated.')
