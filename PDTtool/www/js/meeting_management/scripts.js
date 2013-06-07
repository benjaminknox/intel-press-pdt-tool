$(function(){
/*
	topic_selector = "ul[id='id_topics']"

	//Get the list of topics
	topics_list = $(topic_selector+" > li > label");

	//Hide the topics row in the form table.
	$(topic_selector).parent().parent().hide();

	//Loop through each of the topics.
	topics_list.each(function(){

		//Get the topic element.
		topic_element = $(this);

		//Get the the JSON string.
		json_string = topic_element.text();

		//Append the topic object
		topic_object = $.parseJSON(json_string);

		//Get the checkbox.
		checkbox = topic_element.children('input[name="topics"]');		

		//Check to see if it is checked.
		checked = checkbox.prop('checked');

		//
		$('#topic_selector').append(topic_object.topic_html);

	});
*/
});

function expand_topic(publicid){

	alert(publicid)

}