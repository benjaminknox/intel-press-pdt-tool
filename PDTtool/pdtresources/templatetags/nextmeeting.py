from django import template
from django.shortcuts import render
from meeting_management.resources import get_next_meeting

#Register the template library.
register = template.Library()

#Register the tag name into the templates.
@register.simple_tag(name="sidebarmeeting")
def sidebarmeeting(request):

  nextmeeting = get_next_meeting()

  context = {
    'nextmeeting': nextmeeting,
  }

  template = render(request,'meeting_management/sidebarmeeting.html',context)

  return template.content

#Register the tag name into the templates.
@register.simple_tag(name="nextmeeting")
def sidebarmeeting(request):

  nextmeeting = get_next_meeting()

  context = {
    'nextmeeting':nextmeeting,
  }

  template = render(request,'meeting_management/nextmeeting.html',context)

  return template.content