from django import template
from django.shortcuts import render
from meeting_management.resources import get_next_meeting

######################################################
# fuction load_next_meeting_templat:
#         -Loads the next meeting with the template
#           that is defined.
#   Returns: The template content. 
def load_next_meeting_template(request,template_name):

  #Get the next meeting.
  nextmeeting = get_next_meeting()

  #Check if there is a meeting scheduled in the future.
  if nextmeeting:#If there is a meeting scheduled we return a template.

    #Create context variables for the template.
    context = {
      #Pass in the next meeting.
      'nextmeeting': nextmeeting,
    }

    #Render the template with the context.
    template = render(request,template_name,context)

    #Return the template content.
    return template.content

  #If there is no meeting scheduled at some point
  #     in the future, return an empty string.
  return ""

#Register the template library.
register = template.Library()

#Register the tag name into the templates.
@register.simple_tag(name="sidebarmeeting")
def sidebarmeeting(request):
  #Load the next meeting with the sidebarmeeting.html template.
  return load_next_meeting_template(request,'meeting_management/sidebarmeeting.html')

#Register the tag name into the templates.
@register.simple_tag(name="nextmeeting")
def nextmeeting(request):
  #Load the next meeting with the nextmeeting.html template
  return load_next_meeting_template(request,'meeting_management/nextmeeting.html')