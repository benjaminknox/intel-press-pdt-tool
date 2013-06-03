from django.test import TestCase

# Create your tests here.
class Topic_managementViewsTestCase(TestCase):

  def test_addtopic(self):
      resp = self.client.get('/addtopic/')
      self.assertEqual(resp.status_code, 200)

  def test_viewtopics(self):
      resp = self.client.get('/viewtopics/')
      self.assertEqual(resp.status_code, 200)

  def test_viewtopic(self):
      resp = self.client.get('/viewtopic/')
      self.assertEqual(resp.status_code, 200)

  def test_vi