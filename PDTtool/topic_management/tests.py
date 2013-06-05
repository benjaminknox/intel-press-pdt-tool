#from django.test import TestCase
from pdtresources.testsimplifier import Testsimplifier
from topic_management.context import search_form
from topic_management.forms import TopicForm

# Create your tests here.
class Topic_managementViewsTestCase(Testsimplifier):

  def test_search_form(self):

    class req(object):
      path = '/'
      GET = {}

    req1 = req()

    req2 = req()

    req2.GET = {'search':'test'}

    search_form_list = (search_form(req1),search_form(req2))
    for search_form_text in search_form_list:
      self.assertEquals(search_form_text['search_form'].find('<div id="search_form">'),0)

  def test_MeetingForm(self):
    #topicform = TopicForm()

    #meetingformhtml = meetingform.as_table()

    #print meetingformhtml

    #self.assertContains(meetingformhtml, '{"tawefwefopic_id":')
    pass

  def test_addtopic(self):
    pass

  def test_viewtopics(self):
    pass

  def test_viewtopic(self):
    pass
