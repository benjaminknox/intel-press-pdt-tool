from django.test import TestCase


class User_managementViewTestCase(TestCase):
  
  def test_login(self):
    resp = self.client.get('/login/')
    self.assertEqual(resp.status_code,200)

  def test_logout(self):
    resp = self.client.get('/logout/')
    self.assertEqual(resp.status_code,200)

  def test_register(self):
    resp = self.client.get('/register/')
    self.assertEqual(resp.status_code,200)

  def test_activate(self):
    resp = self.client.get('/activate/')
    self.assertEqual(resp.status_code,200)

  def test_forgotpassword(self):
    resp = self.client.get('/forgotpassword/')
    self.assertEqual(resp.status_code,200) 

  def test_accountsettings(self):
    resp = self.client.get('/accountsettings/')
    self.assertEqual(resp.status_code,200) 

  def test_resetpassword(self):
    resp = self.client.get('/resetpassword/')
    self.assertEqual(resp.status_code,200) 