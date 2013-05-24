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

	if 'currentmeeting' in request.GET:
		action_url += '&currentmeeting=%s'%request.GET['currentmeeting']

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
	content+=		'<button type="submit" class="btn btn-primary lighter-button">Comment</button>'
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
	#Get the parent comment object.
	parentcomment = Comment.objects.get(publicid=parentcommentid)
	#Get the comment text
	comment_text = strip_tags(parentcomment.content)
	
	#If a comment is the highest comment on the child.
	commentclass ='highest_parent_comment' if top_comment else 'child_comment'
	
	#Define the html content of the comment
	content = '<div class="comment_content">'
	#List the name of the comment user.
	content+=	'<h6>%s says:</h6>' % parentcomment.user.get_full_name()
	#Div to wrap the comment body.
	content+=	'<div class="comment_body">'
	#This is the comment text.
	content+= 		comment_text
	#Close the comment body.
	content+=	'</div><!-- .comment_body -->'
	#This is  button to reply to a comment.
	content+=	'<a href="javascript:void(0)" class="btn btn-small reply_button" style="margin-top: -4px;" onclick="$(\'#comment_comment_form_%s\').toggle();">reply</a>'% parentcomment.publicid
	#This fixes floating elements.
	content+= 	'<div class="clear-fix"></div>'
	#Close the comment content.
	content+= '</div><!-- .commetn_content -->'

	#Get the form for this comment box.
	content += comment_form(request,'comment',parentcomment.publicid)

	#Get the list of parents child comments 
	childcomments = parentcomment.comments

	#Check that child comments exist.
	if childcomments.count() > 0:
		#Loop through all the child comments.
		for childcomment in childcomments.all():
			#Create the recursive comments.
			content += recursive_comments(request,childcomment.publicid,False)

	#Create the comments.
	return '<div class="comment_content_wrapper %s pull-right">%s<div class="clear-fix"></div></div><!-- .%s -->'% (commentclass, content,commentclass) 