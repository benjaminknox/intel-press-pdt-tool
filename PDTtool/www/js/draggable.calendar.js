var schedule_droppable_class = '.schedule'
var topic_draggable_item = '.topic'
var topic_list_selector = '.select_topics > .draggable > .topic'

$(function(){
    //Make the sortable div
    $( schedule_droppable_class ).sortable({
      //Stop the dragging classes with .not_draggable
      items: "li:not(.not_draggable)",
      stop: function(event,ui){
          update_schedule_input(ui.item)
      }
    }).droppable({
      drop: dropSchedule
    }).each(function(){
      update_schedule_input($(this));
    });;
    $('.search_topics').keyup(function(){
      search_topics($(this));
    });
    create_draggable_topics();
});

function create_draggable_topics(){
    //Create draggable topics.
  $('.topic').draggable({revert: true,
    helper: 'clone',
    revert: 'invalid',
    //appendTo: '.addmeetingform2',
    zIndex: 1200});
}

function schedule_item_html(publicid,html){
  return '<li class="schedule-item" publicid="'+publicid+'"><i class="icon-minus-sign pull-right" onclick="remove_schedule_item($(this));"></i>'+html+'</li>';
}

function topic_item_html(publicid,html){
  return '<li class="topic schedule-item ui-draggable" publicid="'+publicid+'" id="topic_'+Math.random().toString(36).substring(7)+'_'+publicid+'">'+html+'</li>'
}

function get_meeting_form(object){
  return object.closest('.addmeetingform2');
}

function dropSchedule(event,ui){
  //Get the parent .
  schedule_form = get_meeting_form(ui.draggable);
  //Get the id of the id.
  var id = ui.draggable.attr('id');
  //Get the publicid of the topic
  var publicid = ui.draggable.attr('publicid');
  //If there is an id
  if(id){
    //Check the topic.
    var topic = ui.draggable;
    //Check the children of the scheduler.
    var scheduler = schedule_form.children(schedule_droppable_class);
    //Create some schedule html.
    var schedule_item = schedule_item_html(publicid,topic.html());
    //Insert the scheduleitem.
    scheduler.children('li:last').before(schedule_item);
    //Add a flag for the actual selected-item.
    topic.attr('selected-item','selected');
    //Hide the object.
    $("#"+id).hide();
  }
  update_schedule_input(ui.draggable);
}

function remove_schedule_item(button){
  //Get the schedule_item.
  schedule_item = button.parent();
  //Get the publicid.
  var publicid = schedule_item.attr('publicid');

  //Get the parent.
  parent = get_meeting_form(schedule_item);
  //Get the topics.
  topics = parent.find(topic_list_selector);
  //A flag to see if the topic is present.
  var topic_present = false
  //Show the schedule item.
  topics.each(function(){
    //This is the topic publicid
    var topic_publicid = $(this).attr('publicid');
    //Topic id.
    var topic_id = $(this).attr('id');
    //Check the publicid to see 
    //    if it exists.
    if(topic_publicid == publicid){
      //Show the .selected-item.
      $(this).removeAttr('selected-item').show();
      //The topic is present.
      topic_present = true;
    }
  });

  if(!topic_present){
    //Get the topic item.
    topic_item = schedule_item.clone();
    //Find the topic item.
    topic_item.find('.icon-minus-sign').remove();
    //Get the topic html.
    topic_html = topic_item_html(publicid,topic_item.html());
    //Append to the list.
    topics.parent().append(topic_html);
    //Create the draggable topics.
    create_draggable_topics();
  }

  //Remove the item.
  schedule_item.remove();
  update_schedule_input(button);
}

function update_schedule_input(object){
  meeting_form = get_meeting_form(object);
  modal = meeting_form.parent();
  input = modal.find('input[name="schedule_items"]');
  scheduled_topics = meeting_form.find('.schedule  > .schedule-item');
  var values_string = "";
  scheduled_topics.each(function(){
    var publicid = $(this).attr('publicid');
    if(publicid){
      values_string += publicid+",";
    }
  });
  input.val(values_string);
}

//search_topics searches through the topics availablte
//    to add to the schedule
function search_topics(search_input){
  //Meeting form.
  meeting_form = get_meeting_form(search_input);
  //Get the search value of the input.
  search_value = search_input.val();
  //Get the topics.
  topic = meeting_form.find(topic_list_selector);
  //Hide and loop through each topic.
  topic.hide().each(function(){
    //Show the title
    var title = $(this).text();
    //Check to see if it is a selected-item.
    var selected_item = $(this).attr('selected-item');
    //Get the text value to compare.
    text = title.toLowerCase();
    //Get the search value.
    search = (search_value.length > 0)? search_value.toLowerCase() : 0;
    //Check to see if it is a selected item, and if it matches
    //    the search and the search value.
    if(!selected_item && (text.indexOf(search) != -1 || search == 0)){
      //Show the topic.
      $(this).show();
    }
  });
}
/*$(function(){
    //Make these objects sortable
    $( "#schedule" ).sortable({
      //Stop the dragging classes with .not_draggable
      items: "li:not(.not_draggable)",
      stop: update_schedule_list
    });

    $('.draggable').disableSelection();

    //Create a dropable schedule item.
    $( "#schedule" ).droppable({
      drop: dropSchedule
    });

    //Create draggable topics.
    $('.topic').draggable({revert: true,
      helper: 'clone',
      revert: 'invalid',
      appendTo: '#addmeetingform2',
      zIndex: 999});
    //Create a keyup event for search_topics.
    $('#search_topics').keyup(search_topics);
});

//dropschedule drops an element into the scheduler.
function dropSchedule(event,ui){
  //This is the id attribute of the element
  //    that has been dropped.
  var attribute = ui.draggable.attr('id');
  //This is the publicid of the topic that
  //    has been dropped.
  var publicid = ui.draggable.attr('publicid');
  //Check to see if the object dropped has 
  //    is a topic.
  if(attribute){
    //Get the topic object.
    var topic = $("#"+attribute);
    //Get the schedule item.
    var schedule_item = '<li class="schedule-item" publicid="'+publicid+'"><i class="icon-minus-sign pull-right" onclick="remove_schedule_item($(this));"></i>'+topic.html()+'</li>';

    //Add a flag for the actual selected-item.
    topic.attr('selected-item','selected');
    //Append it before the drag item.
    $("#schedule li:last").before(schedule_item);
    //Hide the object.
    $("#"+attribute).hide();

    update_schedule_list();

  }
}

//search_topics searches through the topics availablte
//    to add to the schedule
function search_topics(event){
  //Get the search value of the input
  search_value = $('#search_topics').val();
  //Hide and loop through each topic.
  $('.topic').hide().each(function(){
    //Show the title
    var title = $(this).text();
    //Check to see if it is a selected-item.
    var selected_item = $(this).attr('selected-item');
    //Get the text value to compare.
    text = title.toLowerCase();
    //Get the search value.
    search = (search_value.length > 0)? search_value.toLowerCase() : 0;
    //Check to see if it is a selected item, and if it matches
    //    the search and the search value.
    if(!selected_item && (text.indexOf(search) != -1 || search == 0)){
      //Show the topic.
      $(this).show();
    }
  });
}

//Remove the schedule item.
function remove_schedule_item(obj){
  //Get the schedule_item dom.
  var schedule_item = obj.parent();
  //Get the publicid.
  var publicid = schedule_item.attr('publicid');
  //Show the schedule item.
  $('.topic').each(function(){
    //This is the topic publicid
    var topic_publicid = $(this).attr('publicid');

    if(topic_publicid == publicid){
      $(this).removeAttr('selected-item').show();
    }
  });
  //Remove the schedule item.
  schedule_item.remove();
  update_schedule_list()
}

function update_schedule_list(){

  var schedule_list = "";

  $('#schedule > li').each(function(){
    var publicid = $(this).attr('publicid');
    if(publicid){
      schedule_list += publicid+",";
    }
  });

  $('input[name="schedule_items"]').val(schedule_list);

}*/