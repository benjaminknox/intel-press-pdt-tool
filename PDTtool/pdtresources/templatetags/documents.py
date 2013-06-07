from django import template
from django.utils.html import conditional_escape as esc

#Register the template library.
register = template.Library()


#Register the tag name into the templates.
@register.simple_tag(name="documents_json")

#################################################################
# function get_document_json: This gets the document information 
#           needed to display each document in a string in JSON
#           format; it is placed into the dom as an attribute.
#   Requires: documents = (PDTtool.topic_management.Document) QuerySet
#   Returns: A JSON string for with document information.
def get_document_json(documents):
  #Define a blank string for the JSON formatted string.
  json = ''
  #Loop through each of the documents in the documents QuerySet.
  for document in documents:
    json += '{' #Start a JSON formatted string
    json += '"publicid":"'+document.publicid+'",'#Pass the publicid of the document.
    json += '"name":"'+document.name+'",'#Pass the name of the document.
    json += '"fileName":"'+document.fileName+'",'#Pass the fileName of the document.
    json += '"comments_count":"%d",'%len(document.comments.all())#Pass the count of the comments on the document.
    json += '"image_url":""'#Pass the image url.
    json += '},'#Close the document string.

  #Remove one character down from the JSON string.
  json = json[:-1]

  #Make a multidimensional PDTtool.topic_management.Document
  #     object JSON string. 
  json = '['+json+']'

  #Escape the JSON string so it can be added to the HTML.
  return esc(json)