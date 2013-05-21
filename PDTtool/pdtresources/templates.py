

# This requires a request variable, formname, and a form.

def output_form_as_table(request,
						 formname,
						 form,
						 submit_text = 'submit',
						 multipart=False,
						 submit_class=True,
						 table_class="form_table",
						 extra_fields="",
						 get_string=""):

	tr_string = lambda string: '<tr><td></td><td>%s<td></tr>'%string
	input_string = lambda inputtype,name,classname=None,value=None: '<input type="%s" name="%s"  class="%s" value="%s" />' % (inputtype,name,classname,value)
	submit_button_string = lambda value,classname="": '<input type="submit" value="%s"  class="btn %s" />' % (value,classname)
	
	form_multipart = ''
	if multipart:
		form_multipart = 'enctype="multipart/form-data"'

	form_string = ""

	form_string+= '<form action="%s?%s" method="POST" %s>' % (request.path,get_string,form_multipart)
	form_string+= input_string('hidden','csrfmiddlewaretoken',value=request.COOKIES['csrftoken'])
	form_string+= input_string('hidden',formname,'1')
	form_string+= '<table class="%s">' % table_class
	form_string+= extra_fields
	form_string+= form
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