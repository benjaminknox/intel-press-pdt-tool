import re 
import time
from django import template
from django.template.defaultfilters import stringfilter

"""
" This isn't used right now.
"""
register = template.Library()

@register.filter
def truncatewords_by_chars(value, arg):
  """
  Truncate words based on the number of characters
  based on original truncatewords filter code
  
  Receives a parameter separated by spaces where each field means:
   - limit: number of characters after which the string is truncated
   - lower bound: if char number is higher than limit, truncate by lower bound
   - higher bound: if char number is less than limit, truncate by higher bound
  """
  from django.utils.text import truncate_words
  try:
    args = arg.split(' ')
    limit = int(args[0])
    lower = int(args[1])
    higher = int(args[2])
  except ValueError: # Invalid literal for int().
    return value
  if len(value) >= limit:
    return truncate_words(value, lower)
  if len(value) < limit:
    return truncate_words(value, higher)

########################################################
# Filter replace: Allows for a regex search and replace
#                     in the template.
@register.filter
def replace ( string, args ): 
    
    #Get the search.
    search  = args.split(args[0])[1]
    #Get the replace.
    replace = args.split(args[0])[2]

    #Search the replace.
    newstring = re.sub( search, replace, string )
    #Return the newstring.
    return newstring

########################################################
# Filter replace: Allows for a regex search and replace
#                     in the template.
@register.filter
def replace_delimeter ( string, args): 

    newstring = string.split(args)[0]

    #Return the newstring.
    return newstring

@register.filter
def epoch(value):
    try:
        return int(time.mktime(value.timetuple())*1000)
    except AttributeError:
        return ''

@register.filter
@stringfilter
def trim(value):
    return value.strip()