from django.core.paginator import Paginator, EmptyPage, InvalidPage

def handle_uploaded_file(f,location):
    with open(location, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return location

#This is a snippet to create pagination objects.
def paginate(request, objects, count=10, param_name='page'):

  #This is a paginator object.
  paginator = Paginator(objects, count)

  #Try the value.
  try:
      #Check the page number.
      pagenum = int(request.GET.get('%s' % param_name, '1'))
  #Except the value.
  except ValueError: 
      #Check the pagenum.
      pagenum = 1

  try:
      #Try to generate the objects.
      result = paginator.page(pagenum)
  except (EmptyPage, InvalidPage):
      #If the page is output the last page.
      result = paginator.page(paginator.num_pages)

  #Create the query
  result.qstring = request.GET.copy()

  #Check the query string for an existing page variable.
  if result.qstring.has_key(param_name):
    #Remove it if it exists.
    del result.qstring[param_name]

  
  #Return the paginator objects.
  return result