from topic_management.models import Comment
from django.utils.html import strip_tags

# This is the form for adding feedback, it used in topic_management.views.viewtopic,
#		and pdtresources.comments.recursive_comments.
#		-It requires a get variable.
#		-It is used to add comments to Topic, Document, and Comment objects.
#		-We can expect topic, document, and comment for commented_object.
def comment_form(request, commented_object = 'topic', commented_object_id=None):

	#Get the commented object id
	commented_object_id_string = str(commented_object_id)
	#Create the name of field
	commented_object_field_name = commented_object+'id'
	#Create an id for the div
	form_div_id = '%s_comment_form_%s' % (commented_object, commented_object_id_string)

	#This gets the page url
	action_url = "%s?publicid=%s"%(request.path,request.GET['publicid'])

	#If it is a topic add a feedback 
	#		button.
	addfeedback = ''
	if commented_object == 'topic':
		#This toggles the form.
		addfeedback+= '<a href="javascript:void(0);" onclick="$(\'#%s\').toggle();">Add Feedback</a>'%form_div_id

			  #Create the comment form.
	content = addfeedback
			  #This is the main style of the div.
	content+= '<div id="%s" class="comment_form">'% form_div_id
				#This is the form wrapper.
	content+= 	'<form action="%s" method="POST">'% action_url
					#This is the CSRF value.
	content+= 		'<input type="hidden" name="csrfmiddlewaretoken" value="%s" />'% request.COOKIES['csrftoken']
					#This is the actual commented object id.
	content+=		'<input type="hidden" name="%s" value="%s" />'% (commented_object_field_name, commented_object_id_string,)
					#this is the textarea for the user input.
	content+=		'<textarea name="content"></textarea><br>'
					#This is the submit button.
	content+=		'<button type="submit" class="btn btn-primary">Go</button>'
				#Close the form.
	content+=	'</form>'
				#Add a height fix for the floating elements.
	content+= 	'<div class="clear-fix"></div> <!-- (bootstrap) .clear-fix -->'
			  #Close the main div style.
	content+= '</div><!-- #%s -->'% form_div_id

	#Return the content form.
	return content


# This function returns the content for a Comment object. It is used
#		recursively to return Comment objects that have a collection 
#		of Comment objects. 
def recursive_comments(request, parentcommentid, top_comment=True):

	parentcomment = Comment.objects.get(publicid=parentcommentid)
	
	comment_text = strip_tags(parentcomment.content)

	if not top_comment:
		commentclass = 'child_comment'
	else:
		commentclass = 'highest_parent_comment'

	content = '<div class="comment_content">'
	content+=	'<h6>'+parentcomment.user.first_name+' '+parentcomment.user.last_name+' says:</h6>'
	content+=	'<div class="comment_body">'
	content+= 		comment_text
	content+=	'</div>'
	content+=	'<a href="javascript:void(0)" class="btn btn-small reply_button" style="margin-top: -4px;" onclick="$(\'#comment_comment_form_%s\').toggle();">reply</a>'% parentcomment.publicid
	content+= 	'<div class="clear-fix"></div>'
	content+= '</div>'

	content += comment_form(request,'comment',parentcomment.publicid)

	childcomments = parentcomment.comments

	if childcomments.count() > 0:

		for childcomment in childcomments.all():

			content += recursive_comments(request,childcomment.publicid,False)

	return '<div class="comment_content_wrapper '+commentclass+' pull-right">'+content+'<div class="clear-fix"></div></div>'