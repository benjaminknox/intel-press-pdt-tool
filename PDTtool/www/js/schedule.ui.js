var category_row_class = 'category-row';
var category_row_selector = '.'+category_row_class;
var scrolling_text_selector = '.scroller';
var scheduler_wrapper_selector = '#scheduler_wrapper';

var meeting_time_left_attr = 'meeting-time-left';
var topic_duration_attr = 'topic-duration';

function scroll(ele){
  var s = ele.text().substr(1)+ele.text().substr(0,1);
  ele.text(s);
}

function start_scrolling(element){
  var scroller = element.find(scrolling_text_selector)
  if(scroller.width() > element.width()){
    intervalID = setInterval(function() {
       scroll(scroller);
    }, 100);
  }else{
    intervalID = false;
  }
}

function stop_scrolling_text(element){
  if(intervalID){
    element.find(scrolling_text_selector).html(element.find('.original-text').html());
    clearInterval(intervalID);
  }
}

function reset_schedule(){
  $('.category-row').each(function(){
    var element = $(this);
    var scheduled_topics = element.find('.category-schedule .topic');
    var unscheduled_topics = element.find('.category .topic');
    var topic_descriptions = element.find('.topic-description');
    scheduled_topics.each(function(){
      var topic = $(this);
      var attr = topic.attr('original-topic');
      var category_element = topic.closest('.category-row').find('.category');
      if(typeof attr !== 'undefined' && attr !== false){
        topic.appendTo(category_element);
      }else{
        topic.remove();
      }
    });

    unscheduled_topics.each(function(){
      var topic = $(this);
      var attr = topic.attr('original-topic');
      if(typeof attr === 'undefined' || attr === false){
        topic.remove();
      }
    });
    topic_descriptions.children('*').html('');
  });
}

function load_meeting_schedule(meeting){
  try{
    var selected_topics = JSON.parse(meeting.attr('meeting-topics'));
   }catch(e){
    console.log(e);
    var selected_topics = null;
   }

  reset_schedule();

  //$(schedule_selector).find('.topic').remove();

  var meeting_duration = meeting.attr('meeting-duration');
  var meeting_time_left = meeting_duration;

  for(i in selected_topics){
    var blank_topic = $('#blank_topic_element .topic').clone();
    var topic = selected_topics[i];
    console.log(selected_topics[i]);
    var category = topic.category.toLowerCase().replace(' ','-')
    var schedule_selector = 'div[schedule-category='+category+']';

    blank_topic.attr('topic-name',topic.name)
               .attr('topic-duration',topic.presentationlength)
               .attr('topic-publicid',topic.publicid)
               .attr('topic-category',category)
               .attr('topic-description',topic.description)
               .attr('topic-user-name',topic.presenter)
               .appendTo(schedule_selector);

    meeting_time_left = meeting_time_left - topic.presentationlength;
    load_topic_information(blank_topic);
  }

  $('#scheduler_wrapper').attr('meeting-duration',meeting_duration)
                         .attr('meeting-time-left',meeting_time_left);

  //This is found in schedule.ui.js
  order_categories();
}

function load_topic_information(topic){
  var topic_name = topic.attr('topic-name');
  var topic_user_name = topic.attr('topic-user-name');
  var topic_description = topic.attr('topic-description');
  var topic_duration = topic.attr('topic-duration');
  var topic_duration_selector = '.topic-duration';
  var topic_name_display_element = topic.closest(category_row_selector).find('.topic-description .topic-name-display');
  var topic_username_display_element = topic.closest(category_row_selector).find('.topic-description .topic-username-display');
  var topic_description_display_element = topic.closest(category_row_selector).find('.topic-description .topic-description-display');
  topic.html('<div class="scroller_wrapper"><span class="scroller">'+topic_name+'&nbsp;&nbsp;&nbsp;</span></div><span class="original-text">'+topic_name+'&nbsp;&nbsp;&nbsp;</span>')
       .append('<div class="topic-duration border-radius-3">'+topic_duration+' min.</div>')
       .hover(function(e){
          var element = $(this);
          var scroller_wrapper = element.find('.scroller_wrapper');
          start_scrolling(scroller_wrapper);
          topic_name_display_element.html(topic_name);
          topic_username_display_element.html(topic_user_name);
          topic_description_display_element.html(topic_description.substring(0, 150)+((topic_description.length > 150)? '...' : ''));
       },function(e){
          stop_scrolling_text($(this));
       });
}

function save_topics(){
  var schedules = $('.category-schedule');
  var publicid = '';
  var category_order = ""
  schedules.each(function(){
    var order = 1
    var schedule = $(this);
    var category_row = schedule.closest('.category-row');
    var scheduler = schedule.closest('#scheduler_wrapper');
    var meeting_duration = parseInt(scheduler.attr('meeting-duration'));
    var current_length = meeting_duration - parseInt(scheduler.attr('meeting-time-left'));
    var category_name = schedule.attr('schedule-category');
    schedule.find('.topic').each(function(){
      var topic = $(this);
      var topic_publicid = topic.attr('topic-publicid');
      if(topic_publicid) publicid += order+'::::'+topic_publicid+',';
      order += 1;
    });
    category_row.find('.meeting_time_total').html("Scheduled Time in Meeting: "+meeting_duration+" minutes<br>Total Meeting Length: "+current_length+" minutes");
    category_order += category_name+',';
  });
  $('#schedule_items_input').val('')
                            .val(publicid);
  $('#schedule_categories_input').val('')
                            .val(category_order);
}

function initial_category_order(){

}

function order_categories(){
  var category_row_element = $(category_row_selector);
  var i = 1;
  category_row_element.each(function(){
    var row = $(this);
    row.find('.order').text(i);
    row.attr('category-order', i);
    i += 1;
  });
  $('.arrow_button').css({'background-position':'','cursor':'pointer'});
  $(category_row_selector+':first .move_up').css({'background-position':'1000px 1000px','cursor':'normal'});
  $(category_row_selector+':last .move_down').css({'background-position':'1000px 1000px','cursor':'normal'});
  save_topics();
}

function populate_schedule_form(){

  var category_time_left_attr = 'category-time-left';

  var schedule_wrapper = $('#scheduler_wrapper');

  var categories = schedule_wrapper.find('.category-row');

  var duration = $('#id_duration').val() * 60;
  var each_category_duration = duration / categories.length;
  var meeting_time_left = duration;

  categories.each(function(){
    var category = $(this);
    category.attr(category_time_left_attr,each_category_duration)
            .attr('category-duration',each_category_duration);
  });
  schedule_wrapper.attr('meeting-duration',duration);
  var there_are_topics = true;
  var topics_will_fit = true;
  while(there_are_topics && topics_will_fit){

    //A variable to check if the categories are filled.
    var categories_filled = false;

    //Loop through the categories and check if they are filled.
    categories.each(function(){
      var category = $(this);
      var schedule_element = category.find('.category-schedule');
      var category_time_left = category.attr(category_time_left_attr);

      var topics_available = category.closest('.category-row').find('.category .topic');
      var could_fill_slot = false;

      //Loop through each topic.
      topics_available.each(function(){
        var topic = $(this);
        var topic_duration = topic.attr(topic_duration_attr);
        var could_place_topic = false;
        if(parseInt(category_time_left) >= parseInt(topic_duration)){
          topic.appendTo(schedule_element);
          could_fill_slot = true;
          category_time_left = category_time_left - topic_duration;
          meeting_time_left = meeting_time_left - topic_duration;
          category.attr(category_time_left_attr,category_time_left);
        }
      });

      //Check if a slot could be filled.
      if(!could_fill_slot) categories_filled = true;

    });

    //Get some more topics
    var topics = schedule_wrapper.find('.category .topic');

    if(categories_filled && meeting_time_left > 0){

      could_fill_slot = false;

      topics.each(function(){
        var topic = $(this);
        var topic_duration = topic.attr(topic_duration_attr);
        var name = topic.attr('topic-name');
        //var time_left = meeting_time_left - topic_duration;
        var schedule_element = topic.closest('.category-row').find('.category-schedule');

        if(parseInt(meeting_time_left) >= parseInt(topic_duration)){
          topic.appendTo(schedule_element);
          meeting_time_left = parseInt(meeting_time_left) - parseInt(topic_duration);
          could_fill_slot = true;
        }

        if(!could_fill_slot){
          topics_will_fit = false;
        }

      });
    }

    if(meeting_time_left <= 0){
      topics_will_fit = false;
    }

    if(topics.length <= 0){
      there_are_topics = false;
    }
    schedule_wrapper.attr(meeting_time_left_attr,meeting_time_left);
  }
}

$('.category').each(function(){
  var category = $(this);
  var category_name = category.attr('category-name');
  var category_name_lower = category_name.toLowerCase().replace(' ','_');
  var header = category.find('.category-title');
  var parent = category.closest(category_row_selector);
  var category_scheduler = parent.find('.category-schedule');

  parent.find('#hidden-category-title').text(category_name);

  header.text(category_name);

  category.find('.topic').each(function(){
    var topic = $(this);
    load_topic_information(topic);
  });
  
  category.sortable({
    cancel:'h4',
    connectWith:category_scheduler,
    receive: function(event,ui){
      var element = $(ui.item);
      var topic_duration = element.attr(topic_duration_attr);
      var scheduler_wrapper = element.closest(scheduler_wrapper_selector);
      var meeting_time_left = scheduler_wrapper.attr(meeting_time_left_attr);
      var new_meeting_time_left = parseInt(meeting_time_left) + parseInt(topic_duration);

      scheduler_wrapper.attr(meeting_time_left_attr,new_meeting_time_left);

      stop_scrolling_text(element);
      start_scrolling(element);
      save_topics();

      move_clearable($(this));
      
    }
  });

  category_scheduler.sortable({
    connectWith:category,
    cancel:'h4',
    receive: function(event,ui){
      var element = $(ui.item);
      var topic_duration = element.attr(topic_duration_attr);
      var scheduler_wrapper = element.closest(scheduler_wrapper_selector);
      var meeting_time_left = scheduler_wrapper.attr(meeting_time_left_attr);
      var new_meeting_time_left = parseInt(meeting_time_left) - parseInt(topic_duration);

      if(new_meeting_time_left < 0){
        element.appendTo(ui.sender);
        alert('There is not enough time left in the meeting for the topic.');

      }else{
        scheduler_wrapper.attr(meeting_time_left_attr,new_meeting_time_left);
        stop_scrolling_text(element);
        start_scrolling(element);
        save_topics();
      }
      move_clearable($(this));
    },
    stop: function(event,ui){
      save_topics();
    },
  });

}).disableSelection();

function move_clearable(element){
  element.find('.clearable').appendTo(element);
}

$('.move_down').click(function(){
var button = $(this);
var category = button.closest(category_row_selector);
var next_category = category.next();
if(next_category.hasClass(category_row_class)){
  category.hide()
          .detach()
          .insertAfter(next_category)
          .fadeIn();
  $(window).scrollTop(category.offset().top - 100);
}
if(!category.next().hasClass(category_row_class)){
  $(this).hide();
}
order_categories();
});

$('.move_up').click(function(){
var button = $(this);
var category = button.closest(category_row_selector);
var prev_category = category.prev();
if(prev_category.hasClass(category_row_class)){
  category.hide()
          .detach()
          .insertBefore(prev_category)
          .fadeIn();
  $(window).scrollTop(category.offset().top - 100);
}
if(!category.prev().hasClass(category_row_class)){
  $(this).hide();
}
order_categories();
});

$('.meeting-item').click(function(){
var meeting = $(this);
});

window_hash = window.location.hash;
if(window_hash){
  publicid = window_hash.replace('#','')
  meeting = $('li['+meeting_publicid_attr+'="'+publicid+'"]');
  load_meeting_schedule(meeting);
}

function order_categories_timer(){
  order_categories();
  var order_categories_t = setTimeout("order_categories_timer()",100);
}

order_categories_timer();

function scroller_function(){
  var scrollPosition = $(document).scrollTop();
  var headerHeight = 130;

  var win = $(window);
  var screen_element = $('.screen');
  var screen_element_height = screen_element.height();
  var screen_element_offset_top = screen_element.offset().top;
  var screen_element_scroll_height = screen_element_offset_top + screen_element_height;

  var wrap_documents_height = $('#wrap_documents').height();
  var document_table_display_height = $('#document_table_display').height();

  var winHeight = win.height();
  var winScrollTop = win.scrollTop();
  var winScreenBottomPosition = winScrollTop + winHeight;

  var submit_element = $('#fixed_update_meeting_element');
  var submit_element_height = submit_element.height();

  if(scrollPosition > headerHeight && wrap_documents_height > document_table_display_height){
    $('#document_table_display').css('margin-top',scrollPosition+"px");
  }else{
    $('#document_table_display').css('margin-top','');
  }
 if(winScreenBottomPosition < screen_element_scroll_height){
  submit_element.css('top',((winScreenBottomPosition - 222) +'px'));
 }else{
  submit_element.css('top','');
 }
  window_loop();
}

scroller_function();

$(window).scroll(function(){
  scroller_function();
});

function view_attendees(){
  $("#view_attendees").toggle("slide",{
    direction:"right"
  })
}