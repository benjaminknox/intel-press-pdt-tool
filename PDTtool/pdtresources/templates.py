from django.shortcuts import render
from django.utils.safestring import mark_safe

#This outputs a form from a form object, I will probably replace 
#			this with a template at some point.
def output_form_as_table(request,
						 formname,
						 form,
						 submit_text = 'submit',
						 multipart=False,
						 submit_class=True,
						 table_class="form_table",
						 extra_fields="",
						 get_string="",
						 add_submit_button=True,
						 formname_value='1',
						 action=False):

	#This is a function for generating a table row string.
	tr_string = lambda string: '<tr><td></td><td>%s<td></tr>'%string
	#This is a function for generating an input string.
	input_string = lambda inputtype,name,classname=None,value=None: '<input type="%s" name="%s"  class="%s" value="%s" />' % (inputtype,name,classname,value)
	#This is a submit button input string.
	submit_button_string = lambda value,classname="": '<input type="submit" value="%s"  class="btn %s" />' % (value,classname)

	#If there is not an action defined by the person
	if not action:
		#Put a string in the action.
		action = "%s?%s" % (request.path,get_string)
		
	form_multipart = ''
	if multipart:
		form_multipart = 'enctype="multipart/form-data"'

	form_string = ""

	form_string+= '<form action="%s" method="POST" %s>' % (action,form_multipart)
	if 'csrftoken' in request.COOKIES:
		form_string+= input_string('hidden','csrfmiddlewaretoken',value=request.COOKIES['csrftoken'])
	form_string+= input_string('hidden',formname,value=formname_value)
	form_string+= extra_fields
	form_string+= '<table class="%s">' % table_class
	form_string+= form
	if add_submit_button:
		form_string+= tr_string(submit_button_string(submit_text))
	form_string+= '</table>'
	form_string+= '</form>'

	return form_string

# This requires a topic object to output properly.
def topic_html(topic):
	publicid = topic.publicid
	html = '<div id="%s" class="topic_option" publicid="%s">' % (topic.id,publicid)
	html+= 		'<div class="topic_title">';
	html+= 		'%s by %s'%(topic.name,topic.user.get_full_name())
	#html+= '<a href="javascript:expand_topic(%s);" class="btn btn-primary btn-mini pull-right">details</a>' % publicid
	html+= 		'</div>'
	html+= 		'<div class="topic_description">';
	html+= topic.description
	html+= 		'</div>'
	html+= '</div>'

	return html

def modal(
				request,
				content,
				modal_title=False,
				modal_id='modal_template',
				modal_form=False,
				modal_class="",
				submit_text='Save Changes',
				submit_button_class='btn-primary',
				close_button_text = 'close',
				close_button_class= ''):

	context = {
		'content': content,
		'modal_title':modal_title,
		'modal_id':modal_id,
		'modal_form':modal_form,
		'modal_class':modal_class,
		'submit_text':submit_text,
		'submit_button_class':submit_button_class,
		'close_button_text': close_button_text,
		'close_button_class': close_button_class,
	}

	return render(request,'resources/modal.html',context)

#This is an interface between the table and 
#			modal, it links the two together.
def form_modal(request,
							 formname,
							 form,
							 modal_title=False,
							 modal_id='modal_template',
							 modal_class="",
							 multipart=False,
							 submit_class=True,
							 table_class="modal_form_table",
							 extra_fields="",
							 get_string="",
							 formname_value="1",
							 action=False,
							 add_submit_button=False,
							 submit_text='Save Changes',
							 submit_button_class='btn-primary',
							 close_button_text='close',
							 close_button_class=''):

	#Get the actual form.
	form = mark_safe(output_form_as_table(
												 request,
												 formname,
												 form,
												 submit_text = submit_text,
												 multipart=multipart,
												 submit_class=submit_class,
												 table_class=table_class,
												 extra_fields=extra_fields,
												 get_string=get_string,
												 add_submit_button=add_submit_button,
												 formname_value=formname_value,
												 action=action)
				 )


	#Get the modal
	returned_modal = modal(
												request,
												form,
												modal_title=modal_title,
												modal_id=modal_id,
												modal_form=True,
												modal_class=modal_class,
												submit_text=submit_text,
												submit_button_class=submit_button_class,
												close_button_text=close_button_text,
												close_button_class=close_button_class)

	return mark_safe(returned_modal.content)