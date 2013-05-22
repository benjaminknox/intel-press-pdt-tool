$(function(){
    $( "#schedule" ).sortable({
      items: "li:not(.not_draggable)"
    });
    $( "#schedule" ).disableSelection().droppable({
      drop: dropSchedule
    });
    $('.topic').draggable({revert: true});
    $('#search_topics').keyup(search_topics);
});

function dropSchedule(event,ui){
  var attribute = ui.draggable.attr('id');
  var publicid = ui.draggable.attr('publicid');
  if(attribute){
    var topic = $("#"+attribute);
    var schedule_item = '<li class="schedule-item" publicid="'+publicid+'">'+topic.html()+'</li>';

    topic.attr('selected-item','selected');

    $("#schedule li:last").before(schedule_item);

    $("#"+attribute).hide();
  }
}

function search_topics(event){
  search_value = $('#search_topics').val();

  $('.topic').hide().each(function(){
    
    var title = $(this).text();
    var selected_item = $(this).attr('selected-item');

    text = title.toLowerCase();

    search = (search_value.length > 0)? search_value.toLowerCase() : 0;

    if(!selected_item && (text.indexOf(search) != -1 || search == 0)){
      $(this).show();
    }

  });
}