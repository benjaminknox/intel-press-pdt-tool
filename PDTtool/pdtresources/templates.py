from django.shortcuts import render
from django.utils.safestring import mark_safe

###
#This simply creates an html input string.
def input_string(inputtype,
								 name,
								 classname=None,
								 value=None):
	
	###
	#Get the value of the string.
	value = '''<input type="%s" name="%s"  class="%s" value="%s" />''' % (inputtype,
																														 name,
																														 classname,
																														 value)

	###
	#Return the value.
	return mark_safe(value)

###
#This creates a submit input string.
def submit_button_string(value,classname=""):
	return '<input type="submit" value="%s"  class="btn %s" />' % (value,classname)

###
#This creates a row in a database table
def tr_string(string):
	return '<tr><td></td><td>%s<td></tr>'%string

###
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
						 action=False,
						 method="POST",
						 hidden_fields=None):

	###
	#Create a new list reference for the hidden_fields.
	if hidden_fields:
		hidden_fields_list = hidden_fields
	else:
		hidden_fields_list = []

	###
	#Load in hidden fields
	#This is a hidden field to identify the field name.
	hidden_fields_list.append(input_string('hidden',formname,value=formname_value))

	###
	#If there is not an action defined create 
	#		one based on the current path.
	if not action:
		#Get the request url.
		action = "%s?%s" % (request.path,get_string)

	###
	#If the form is flagged as multipart (has file data),
	#		add in the tag below
	if multipart:
		formmultipart = mark_safe('enctype="multipart/form-data"')
	else:
		formmultipart = ''

	###
	#If there needs to be a submit button create a string
	if add_submit_button:
		add_submit_button = tr_string(submit_button_string(submit_text))
	else:
		add_submit_button = ''

	###
	#Pass variables into the template context.
	context = {
			'formname':formname,
			'action':action,
			'method':method,
			'formmultipart':formmultipart,
			'hidden_fields':hidden_fields_list,
			'table_class':table_class,
			'extra_fields':extra_fields,
			'form':form,
			'add_submit_button': add_submit_button
		}

	###
	#Get the template as a string.	
	template = mark_safe(
											#Render the form template using the context variables.
											render(
														#Load the request
														request,
														#Load the template.
														'resources/forms.html',
														context
												#Output the file.
											).content
						 )
	###
	#Return the rendered template.
	return template

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