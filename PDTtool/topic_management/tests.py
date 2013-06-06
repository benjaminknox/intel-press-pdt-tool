#from django.test import TestCase
import os
import PDTtool.settings as settings
from topic_management.forms import TopicForm
from meeting_management.models import Meeting
from user_management.models import ExtendedUser
from topic_management.context import search_form
from topic_management.models import Topic, Document
from pdtresources.testsimplifier import Client,Testsimplifier

# Create your tests here.
class Topic_managementViewsTestCase(Testsimplifier):

  def create_topics(self,extuser=False,username='topic.owner'):

    if not extuser:
      extuser = self.create_user(username, groups = ('Program Manager',))

    topic1 = Topic(
                  user=extuser.user,
                  name='Topic1',
                  category='Outline',
                  topic_slug='UNIQUEVL',
                  )

    topic2 = Topic(
                  user=extuser.user,
                  name='Topic2',
                  category='Outline',
                  topic_slug='OTHER',
                  )

    topic1.save()
    topic2.save()

    document1 = Document(
              location='fakepath',
              name='Document1 A Document Name XCVF',
              fileName='fakepath/doc.docx',
              size=200,
              topic=topic1,
      )

    document1.save()

    document2 = Document(
              location='fakepath',
              name='Document2 A Document Name XCVF',
              fileName='fakepath/doc.docx',
              size=200,
              topic=topic1,
      )

    document2.save()

    topic1.documents.add(document1,document2)

    document3 = Document(
              location='fakepath',
              name='Document3 A Document Name XCVF',
              fileName='fakepath/doc.docx',
              size=200,
              topic=topic2,
    )
    document4 = Document(
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

    self.create_topics()
  
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

    self.add_topic_form(C)

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

    del resp

    #Logout the user.
    C.logout()

   #self.create_topics(extuser=ExtendedUser.objects.get(user__username='topic.owner'))

    #Get a topic to test with
    topic = Topic.objects.get(name='Topic1')
    topic_publicid = topic.publicid
    document = topic.documents.get(name__icontains='Document1')
    document_publicid = document.publicid
    document_text = 'A Document Name XCVF'

    #Check the mytopics variable is working.
    C = Client()

    comment_content = 'COMMENT TEXT'

    #Create postData for the url.
    postData = {
      'topicid':topic_publicid,
      'content':comment_content
    }
    #Get the url for the topic.
    topic_url = "%s?publicid=%s" % (url,topic_publicid)
    
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
    self.checkRespContains(resp, comment_content)
    #The string below will only exist if the documents 
    #   loaded right.
    self.checkRespContains(resp, document_text)

    del resp

    document_comment_content = 'COMMENT ON DOCUMENT TEXT'

    #Create postData for the url.
    postData = {
      'documentid':document_publicid,
      'content':document_comment_content
    }
    #A comment on the document should post to the page
    #   the page with the content listed above.
    resp = C.post(topic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    #The string below will only exist if the post to the 
    #   database was successful for the topic.
    self.checkRespContains(resp, document_comment_content)

    del resp

    #Get the comment we just posted and test a comment reply.
    comment = document.comments.get(content=document_comment_content)
    comment_publicid = comment.publicid

    comment_reply_content = 'COMMENT REPLY TEXT'

    #Create postData for the url.
    postData = {
      'commentid':comment_publicid,
      'content':comment_reply_content,
    }
    #A reply to the comment should post to the page below.
    resp = C.post(topic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    #The string below will only exist if the post to the 
    #   database was successful for the topic.
    self.checkRespContains(resp, comment_reply_content)

    del resp

    C.logout()

    C.login(username='topic.owner',password='test')

    topic_description = 'update DESCRIPTION TEST'

    #Create postData for the url.
    postData = {
      'update_topic_description':topic_publicid,
      'description':topic_description,

    }
    #A reply to the comment should post to the page below.
    resp = C.post(topic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    #The string below will only exist if the post to the 
    #   database was successful for the topic.
    self.checkRespContains(resp, topic_description)

    del resp

    #A reply to the comment should post to the page below.
    resp = C.get(url,{'publicid':'nopublicid'})
    #Check the redirect
    self.checkRedirects(resp,urlstring='/viewtopics/')

    del resp

    presentation_length = '30'
    release_update_value = "%s minute presentation" % presentation_length

    #Create postData for the url.
    postData = {
      'topic_ready_for_review_id':topic_publicid,
      'topic_presentationlength':presentation_length,

    }
    #A test to release the topic to being able to be
    #   dragged into the meeting schedule.
    resp = C.post(topic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    #The string below will only exist if the post to the 
    #   database was successful for the topic.
    self.checkRespContains(resp, release_update_value)

    del resp

    extuser = self.create_user('user.name')

    #Create a meeting to test the update of a topic release.
    meeting = Meeting(
                      name='Meeting Name',
                      description='Meeting Description',
                      duedate='2013-05-05',
                      startdate='2013-05-05',
                      starttime='13:00:00',
                      user=extuser.user,
                      maxscheduleitems=8,
                      duration=0
                      )
    meeting.save()
    topic.meeting = meeting
    meeting.topics.add(topic)
    topic.save()

    #Create postData for the url.
    postData = {
      'topic_ready_for_review_id':topic_publicid,

    }
    #A test to unrelease the topic.
    resp = C.post(topic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    #The string below will only exist if the post to the 
    #   database was successful for the topic.
    self.checkRespNotContains(resp, release_update_value)

    del resp

    #Create postData for the url.
    postData = {
      'deleted_documentid':document_publicid,
    }
    #A test to unrelease the topic.
    resp = C.post(topic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    #The string below will only exist if the post to the 
    #   database was successful for the topic.
    self.checkRespNotContains(resp, 'Document1 %s' % document_text)

    del resp

    #Upload a new document.
    newtopic = self.add_topic_form(C)
    newtopic_publicid = newtopic.publicid
    newdocument = newtopic.documents.all()[0]
    newdocument_publicid = newdocument.publicid

    newtopic_url = "/viewtopic/?publicid=%s" % newtopic_publicid

    #Test the update of a document
    file = "%s/www/css/style.css" % settings.BASE_DIR
    with open(file) as fp:

      #Create postData for the url.
      postData = {
        'updated_documentid':newdocument_publicid,
        'file':fp,
      }
      resp = C.post(newtopic_url,postData)
      #self.checkRedirects(resp,'/viewtopics/')
      self.checkTemplateUsed(resp, template)
      #The string below will only exist if the post to the 
      #   database was successful for the topic.
      self.checkRespContains(resp, 'style.css')

      del resp


    ###
    # Test the download.
    ###

    downloaddocument = newtopic.documents.all()[0]

    document_filename = downloaddocument.fileName

    download_url = '/download/%s/%s' % (newtopic_publicid,document_filename)

    resp = C.get(download_url)

    self.assertIn(document_filename, resp['Content-Disposition'])

    del resp

    #Test the adding of a document.
    file = "%s/www/js/jquery.min.js" % settings.BASE_DIR
    with open(file) as fp:

      #Create postData for the url.
      postData = {
        'add_document':'1',
        'file':fp,
      }
      resp = C.post(newtopic_url,postData)
      #self.checkRedirects(resp,'/viewtopics/')
      self.checkTemplateUsed(resp, template)
      #The string below will only exist if the post to the 
      #   database was successful for the topic.
      self.checkRespContains(resp, 'jquery.min.js')

      del resp

    #Logout the user.
    C.logout()

    #Create a supervisor
    self.create_user(username='test.supervisor',groups=('Supervisor','Program Manager',))

    #Login the supervisor
    C.login(username='test.supervisor',password='test')

    #Create postData for the url.
    postData = {
      'released_topicid':newtopic_publicid,
    }
    #A test to aprove the topic.
    resp = C.post(newtopic_url,postData)
    #self.checkRedirects(resp,'/viewtopics/')
    self.checkTemplateUsed(resp, template)
    self.assertTrue(os.path.exists("%s/%s" % (settings.APPROVED_TOPIC_DIR,newtopic_publicid)))

    del resp


    #Upload a new document.
    newtopic2 = self.add_topic_form(C,description='Testing')
    newtopic2_publicid = newtopic2.publicid

    newtopic2_url = "/viewtopic/?publicid=%s" % newtopic2_publicid

    #Create postData for the url. 
    postData = {
      'deleted_topicid':newtopic2_publicid,
    }

    #A test to aprove the topic.
    resp = C.post(newtopic2_url,postData)

    #self.checkRedirects(resp,'/viewtopics/')
    self.assertIn('viewtopics/?deleted',resp['Location'])
    self.assertFalse(os.path.exists("%s/%s" % (settings.UPLOADED_TOPIC_DIR,newtopic2_publicid)))
    self.assertTrue(os.path.exists("%s/%s" % (settings.DELETED_TOPIC_DIR,newtopic2_publicid)))

    del resp

    #Logout the user.
    C.logout()
