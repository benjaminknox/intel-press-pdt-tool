#from django.test import TestCase
from topic_management.forms import TopicForm
from topic_management.context import search_form
from pdtresources.testsimplifier import Client,Testsimplifier
from topic_management.models import Topic, Document
from user_management.models import ExtendedUser

# Create your tests here.
class Topic_managementViewsTestCase(Testsimplifier):

  def create_topics(self,extuser=False,username='topic.owner'):

    if not extuser:
      extuser = self.create_user(username)

    topic1 = Topic(
                  user=extuser.user,
                  name='This is the document',
                  category='Outline',
                  topic_slug='UNIQUEVL',
                  )

    topic2 = Topic(
                  user=extuser.user,
                  name='This is the document',
                  category='Outline',
                  topic_slug='OTHER',
                  )

    topic1.save()
    topic2.save()

    document1 = Document(
              user=extuser.user,
              location='fakepath',
              name='Document1 A Document Name XCVF',
              fileName='fakepath/doc.docx',
              size=200,
              topic=topic1,
      )

    document1.save()

    document2 = Document(
              user=extuser.user,
              location='fakepath',
              name='Document2 A Document Name XCVF',
              fileName='fakepath/doc.docx',
              size=200,
              topic=topic1,
      )
    document2.save()
    topic1.documents.add(document1,document2)

    document3 = Document(
              user=extuser.user,
              location='fakepath',
              name='Document3 A Document Name XCVF',
              fileName='fakepath/doc.docx',
              size=200,
              topic=topic2,
    )
    document4 = Document(
              user=extuser.user,
              location='fakepath',
              name='Document4 A Document Name XCVF',
              fileName='fakepath/doc.docx',
              size=200,
              topic=topic2,
    )

    document3.save()
    document4.save()
    topic2.documents.add(document3,document4)

  def setUp(self):
    super(Topic_managementViewsTestCase,self).setUp()
    
    extuser = self.create_user('topic.owner')

    self.create_topics(extuser=extuser)
  

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

  def test_addtopic(self):

    url = '/addtopic/'
    redirect_url = '/login/?next=/addtopic/'

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
    self.checkRedirects(resp,redirect_url,target_status_code=302)
    #Logout the user.
    C.logout()

    del resp

    #Login a user.
    self.create_user('test.pmanager',groups=('Program Manager',))
    C.login(username='test.pmanager',password='test')
    resp = C.get(url)
    self.checkTemplateUsed(resp,'topic_management/addtopic.html')

    #Check the return of an invalid form.
    postData = {
      'name':'',
      'description':'',
      'category':'',
    }
    resp = C.post(url,postData)
    self.checkTemplateUsed(resp,'topic_management/addtopic.html')

    #Check the return of an invalid form.
    postData = {
      'name':'test',
      'description':'test',
      'category':'Outline',
    }
    resp = C.post(url,postData)
    self.assertEquals(resp.status_code, 302)  
    #self.checkTemplateUsed(resp,'topic_management/addtopic.html')
    

    #Logout the user.
    C.logout()

  def test_viewtopics(self):   
    
    url = '/viewtopics/'
    redirect_url = '/login/?next=/viewtopics/'
    template = 'topic_management/viewtopics.html'

    #Check the redirect when a user is not logged in.
    resp = self.client.get(url)
    self.checkRedirects(resp, redirect_url)

    del resp

    #Check that a logged in user can see the topics
    #   that have been inserted into the databse.
    C = Client()
    #Login a user.
    C.login(username='test.user',password='test')
    resp = C.get(url)
    self.checkTemplateUsed(resp, template)
    self.checkRespContains(resp,'OTHER')
    #Logout the user.
    C.logout()

    del resp

    #Check that the search get variable works.
    C = Client()
    C.login(username='test.user',password='test')
    resp = C.get(url,{'search':'UNIQUEVAL'})
    self.checkRespNotContains(resp,'OTHER')
    self.checkRespContains(resp,'UNIQUEVAL')
    #Logout the user.
    C.logout()

    del resp

    #Check the mytopics variable is working.
    C = Client()
    C.login(username='topic.owner',password='test')
    resp = C.get(url,{'mytopics':'1'})
    self.checkRespContains(resp,'OTHER')
    self.checkTemplateUsed(resp, template)
    #Logout the user.
    C.logout()

    del resp

    #Delete all of the topic objects.
    Topic.objects.all().delete()

    #Check that an empty viewtopics is loading properly.
    C = Client()
    #Login a user.
    C.login(username='test.user',password='test')
    resp = C.get(url,{'page':'30'})
    self.checkTemplateUsed(resp, template)
    self.checkRespContains(resp,'No results found')
    #Logout the user.
    C.logout()

    del resp

  def test_viewtopic(self):
    
    url = '/viewtopic/'
    redirect_url = '/login/?next=/viewtopic/'
    template = 'topic_management/viewtopic.html'

    #Check the redirect when a user is not logged in.
    resp = self.client.get(url)
    self.checkRedirects(resp, redirect_url)

    del resp

    #Check the redirect to viewing topics when there 
    #   we go to a topic that doesn't exist.
    C = Client()
    C.login(username='test.user',password='test')
    resp = C.get(url)
    self.checkRedirects(resp,'/viewtopics/')
    #self.checkTemplateUsed(resp, template)
    #Logout the user.
    C.logout()

    del resp

    self.create_topics(extuser=ExtendedUser.objects.get(user__username='topic.owner'))

    #Get a topic to test with
    topic = Topic.objects.all().values()[0]

    #Check the mytopics variable is working.
    C = Client()

    #Create postData for the url.
    postData = {
      'topicid':topic['publicid'],
      'content':'COMMENT TEXT'
    }
    #Get the url for the topic.
    topic_url = "%s?publicid=%s" % (url,topic['publicid'])
    
    #We should not be able to edit the topic being
    #   logged in as a user that doesn't own it.
    #We should be able to see a comment that we add
    #   with a POST.
    #It should also contain at least on document.
    C.login(username='test.user',password='test')
    resp = C.post(topic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    #The string below will only show up if we own the topic
    #   and we are a supervisor.
    self.checkRespNotContains(resp, 'Presentation Length: ')
    #The string below will only exist if the post to the 
    #   database was successful for the topic.
    self.checkRespContains(resp, 'COMMENT TEXT')
    #The string below will only exist if the documents 
    #   loaded right.
    self.checkRespContains(resp, 'A Document Name XCVF')
    #Logout the user.
    C.logout()

    del resp