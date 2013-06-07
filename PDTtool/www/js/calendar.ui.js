var calendar_rows_selector = '#calendar-wrapper .month tr';
var calendar_cell_selector = calendar_rows_selector+' td';
var calendar_cell_wrapper_selector = calendar_cell_selector+" .cell_wrapper_selector";
var calendar_today_cell_bgcolor = '#EEE';
var calendar_day_form_selector = '.calendar_day_form';
var calendar_day_form_copy_class = 'calendar_day_form_copy';
var calendar_day_form_copy_selector = '.'+calendar_day_form_copy_class;

var screen_class = 'screen';
var screen_selector = '.'+screen_class;
var add_forms_selector = screen_selector;

var meeting_form_id = 'add_meeting_form';
var meeting_form_selector = '#'+meeting_form_id;
var meeting_form_header_selector = meeting_form_selector+" h3";
var meeting_form_table_id = 'meeting_form_table';
var meeting_form_table_selector = '#'+meeting_form_table_id;

var schedule_form_id = 'add_schedule_form';
var schedule_form_selector = '#'+schedule_form_id;
var schedule_form_header_selector = schedule_form_selector+" h3";

var cell_selected_bgcolor = '#FFF6E9';
var cell_display_height = 21;

var opened_cell_class = 'opened_cell';
var opened_cell_selector = '.'+opened_cell_class;
var opened_cell_extra_width = 10;

var cell_info_class = 'cell_info'
var cell_info_selector = '.'+cell_info_class;
var hide_cell_info_class = 'hide-cell-info';
var hide_cell_info_selector = '.'+hide_cell_info_class;


var sidebar_selector = '#sidebar'
var scheduled_topic_in_meeting_class = 'scheduled_topic_in_meeting'
var scheduled_topic_in_meeting_selector = '.'+scheduled_topic_in_meeting_class

var meeting_publicid_attr = 'meeting-publicid';

var topic_publicid_attr = 'topic-publicid';
var topic_name_attr = 'topic-name';
var topic_description_attr = 'topic-description';
var topic_documents_attr = 'topic-documents';
var topic_meeting_publicid_attr = 'topic-meeting-publicid';

var schedule_wrapper_class = 'schedule_wrapper';
var schedule_wrapper_selector = '#'+schedule_wrapper_class;

var droppable_class = 'droppable';

var available_topics_class = 'available_topics';
var available_topics_selector = '.'+available_topics_class;
var available_topics_droppable_selector = available_topics_selector+' .'+droppable_class;

var select_topics_class = 'select_topics';
var select_topics_selector = '.'+select_topics_class;
var select_topics_droppable_selector = select_topics_selector+' .'+droppable_class;

var schedule_grid_class = 'create_schedule';
var schedule_grid_selector = '.'+schedule_grid_class;
var create_schedule_droppable_selector = schedule_grid_selector+' .'+droppable_class;

var schedule_input_selector = '#schedule_items_input';

var edit_form_button_selector = ".edit_form_button";
var delete_meeting_input_selector = "#delete_meeting_input";

var meeting_submit_button_class = "meeting_submit_button";
var meeting_submit_button_selector = "."+meeting_submit_button_class;


//This is a hidden input in the meeting form,
//    the idea is that it will let the backend
//    script know if we are editing a meeting 
//    or if we are adding a new meeting.
var meeting_form_identity_selector = '#meeting_form_identity';

function toggle_screen(screen_id){
  screen_selector_element = $(screen_selector);
  
  screen_selector_element.toggle();

  if (screen_id) show_screen(screen_id);

}
function show_screen(screen_id){
  $(screen_selector+' .screen-content').hide();
  $('#'+screen_id).show();

  if($(screen_selector).is(':visible')){
    $('.black_overlay').show();
  }else{
    $('.black_overlay').hide();
  }

  window_loop();

}
function window_loop(){

  //Get the screen element
  var screen_element = $('.screen');

  //Get the window height
  win = $(window);
  minWinHeight = 700;
  minWinWidth= 730;
  winHeight = win.height();
  winWidth = win.width();

  htmlSelector = $("HTML,BODY");
  if(winHeight < minWinHeight){
    htmlSelector.height(minWinHeight);
    winHeight = minWinHeight
  }else{
    htmlSelector.height('100%');
  }
  if(winWidth < minWinWidth){
    htmlSelector.width(minWinWidth);
  }else{
    htmlSelector.width('100%');
  }

  //Get the navbarheight.
  navbarHeight = $('#navbar').height();
  //Get the infobarheight.
  infobarHeight = $('#infobar').height();
  //Get the page header height, #navbar+#infobar.
  headerHeight = navbarHeight + infobarHeight;
  //Calculate the display height for the calendar.
  displayHeight = winHeight - headerHeight - 160;
  //Get the calendar row count.
  calendarRowCount = $(calendar_rows_selector).length;
  //Get the calendar row height.
  calendarRowHeight = displayHeight / (calendarRowCount - 2);
  //Select the calendar cells.
  calendar_cell = $(calendar_cell_selector);
  //Get the calendar cell width.
  calendarCellWidth = calendar_cell.width();
  //Assign the day highlight widht and height.
  $(calendar_cell_wrapper_selector).height(calendarRowHeight - 23 )
                                   .width(calendarCellWidth +1 )
                                   .each(function(){
                                    adjust_meeting_info($(this));
                                   });
  $(opened_cell_selector).width(calendarCellWidth + opened_cell_extra_width);
  //ajdust the meeting width.
  adjust_meeting_width();
  //Ajdust the calendar row height.
  $(calendar_cell_selector).parent().height(calendarRowHeight);

  $('#schedule_wrapper_scroller').css({'max-height':winHeight * .40 + 'px'});

  adjust_schedule();

  var overlay_height = displayHeight+128
  if(screen_element.is(":visible")){

    var screen_element_from_top =  screen_element.offset().top

    var screen_element_height = $('.screen').height() + screen_element_from_top;

    if(overlay_height < screen_element_height){
      overlay_height = overlay_height + (screen_element_height - overlay_height)
    }
  }

  $('.black_overlay').height(overlay_height).css({'top':headerHeight+2+'px'});

  var t = setTimeout("", 1000)

  $('#calendar-wrapper').css('margin-top','20px');

  $('#loading').hide();
}
function adjust_meeting_width(){
  $(calendar_cell_selector).find('li').each(function(){
    var meeting = $(this)
    var parentdiv = $(this).closest('div');
    var width = parentdiv.width();
    if(parentdiv.hasClass(opened_cell_class)){
      var margin = 26;
    }else{
      var margin = 16;
    }
    meeting.width(width - margin);
  });
}
function adjust_meeting_info(cell){
  var meetings = cell.find('li');
  var cell_info = cell.find(cell_info_selector);
  var meetingsCount = meetings.length + 3;
  var cellDisplayHeight = parseInt(cell.height()) - cell_display_height;
  var meetingsTotalHeight = 0;
  var hiddenMeetingsAmt = 0;
  meetings.each(function(){
    var meeting = $(this);
    var height = parseInt(meeting.height());
    var text = meeting.text();
    var meetinghtml = '';
    meetingsTotalHeight += height;
    if(cellDisplayHeight < meetingsTotalHeight && !cell.hasClass(opened_cell_class)){
      $(this).hide();
      hiddenMeetingsAmt++;
    }else{
      $(this).show();
    }
  });
  if(hiddenMeetingsAmt > 0){
    cell_info.html(hiddenMeetingsAmt+' more');
    cell_info.show();
   }else{
    cell_info.hide();
  }
}
function make_cell_background(calendar_cells){
  calendar_cells.each(function(){
    var cell = $(this);
    if(cell.hasClass('highlight')){
      $(this).css({'background':calendar_today_cell_bgcolor});
    }else{
      $(this).css({'background':'inherit'});
    }
  });
}
function add_meeting_form_submit(form){

  $('#submit_meeting_info_button').hide();
  $('#edit_schedule_button').show();

  fill_meeting_form();
  populate_topics_selector();
  var name_input_selector = 'input[name="name"]';
  var startdate_input_selector = 'input[name="startdate"]';
  var duedate_input_selector = 'input[name="duedate"]';
  var name = form.find(name_input_selector).val();
  var startdate = form.find(startdate_input_selector).val();
  var duedate = form.find(duedate_input_selector).val();
  var add_forms_element = $(add_forms_selector);

  add_forms_element.find(name_input_selector).val(name);
  add_forms_element.find(duedate_input_selector).val(duedate);
  add_forms_element.find(startdate_input_selector).val(startdate);
  
  form.closest('.calendar_day_form').remove();

  toggle_screen('add_meeting_form');

  return false;
}
function remove_form_add_meeting(){
   $(calendar_day_form_copy_selector).remove();
}
function close_opened_cell(){
    $(opened_cell_selector).each(function(e){
      var cell = $(this);
      var cell_info = cell.find(cell_info_selector);
      cell.addClass('cell_wrapper_selector')
          .addClass('light-hard-shadow')
          .removeClass(opened_cell_class)
          .removeClass('light-hard-shadow');
      var parent_td = cell.closest('td');
      var newCellWidth  = cell.width() - opened_cell_extra_width;
      var newCellHeight = parent_td.height() - cell_display_height;
      if(parent_td.hasClass('today')){
        var bgcolor = calendar_today_cell_bgcolor;
      }else{
        var bgcolor = 'inherit';
      }
      cell.width(newCellWidth)
          .height(newCellHeight)
          .css({'padding-left':'0','background':bgcolor});
      adjust_meeting_info(cell);
    });
}
function cell_info_click(){
  //When you click on the more meetings button.
  $(cell_info_selector).click(function(e){
    var cell_info = $
    var cell_info = $(this);
    var cell = cell_info.closest('.cell_wrapper');
    close_opened_cell();
    var cell_height = cell.height();
    var cell_padding = 4 + 20;
    var cell_height = cell.height() - cell_padding;
    var meetings_height = 0;
    var i = 0;
    cell.find('li').each(function(){
      meetings_height += $(this).height();
      i++;
    });
    meetings_height += cell_padding; 
    if(cell_height > meetings_height){
      cell_info.removeClass(hide_cell_info_class);
    }
    if(cell_height <= meetings_height && !cell_info.hasClass(hide_cell_info_class)){
      cell.height((i * 24) + 18);
      cell.addClass(opened_cell_class).addClass('light-hard-shadow').removeClass('cell_wrapper_selector');
      cell.find('li').show();
      cell_info.text('Hide');
      cell_info.addClass(hide_cell_info_class);
      var newCellWidth  = cell.width() + opened_cell_extra_width;
      cell.width(newCellWidth).css({'padding-left':'10px','background':cell_selected_bgcolor});
    }else{
      close_opened_cell();
      cell_info.removeClass(hide_cell_info_class);
      adjust_meeting_width();
    }
    e.stopPropagation();
  });
}

function check_meeting_info_form(submit_bool){
  var meeting_form_table = $('#meeting_form_table');

  var meeting_info_inputs = meeting_form_table.find('input,textarea');

  var invalid = false;

  var fieldcheckstr = "";

  meeting_info_inputs.each(function(){
        //Get the feild.
        var field = $(this)
        //Get the field class.
        var fieldclass = field.attr('class');
        //Get the field id.
        var fieldid = field.attr('id');
        //Get the field name.
        var fieldname = field.attr('name')
        //Get the field value.
        var fieldvalue = field.val();
        //Get the field label.
        var fieldlabel = meeting_form_table.find('label[for="'+fieldid+'"]').text();
        //Define a string for the start of the field error report.
        var error_start = 'For the '+fieldlabel.toLowerCase().replace(':','');
        //Make sure there is a name
        if(
          //Check the field id.
          fieldid == 'id_name' &&
          //Check the length field value.
          fieldvalue.length == 0
        ){
          //Output a field error string.
          fieldcheckstr +=  error_start+', please enter a value. \r\n';
          //Flag the form invalid.
          invalid = true;
        }

        //Check the date fields.
        if(
          //Check if the field has a class.
          fieldclass && 
          //Check the class is datepicker.
          fieldclass.indexOf('datepicker') != -1 &&
          ( 
            //Check the field value matches a date pattern.
            !fieldvalue.match(/(\d{4})-(\d|\d{2})-(\d|\d{2})/) ||
            //Check the fieldvalue is longer than ten.
            fieldvalue.length > 10
          )
        ){
          //Output a field error string.
          fieldcheckstr += error_start+', please use this format: yyyy-mm-dd \r\n';
          //Flag the form invalid.
          invalid = true;
        }

        //Check the time fields.
        if(
          //Check if the field has a class.
          fieldclass &&
          //Check the class is timepicker.
          fieldclass.indexOf('timepicker') != -1 &&
          //Check the value matches the time 
          //    below appropriately.
          !fieldvalue.match(/(\d|\d{2}):(\d{2})(am|pm)/)
        ){
          //Output a field error string.
          fieldcheckstr +=  error_start+', please use this format: 00:00am/pm \r\n';
          //Flag the form invalid.
          invalid = true;
        }
  });

  //If the form is invalid do this:
  if(invalid){
    //Alert the errors.
    alert(fieldcheckstr);
  }

  if(submit_bool && !invalid){
    meeting_form_table.closest('form').submit();
   }else{
    return invalid;
  }

}

function load_schedule_form(){
  load_schedule_form_populate_schedules(false);
}

function load_schedule_form_populate_schedules(new_schedule){

  if(check_meeting_info_form(false)){
    return false;
  }

  $(schedule_form_selector).show();
  $(meeting_form_selector).hide();
  //This is found in schedule.ui.js
  reset_schedule();
  
  if(new_schedule){
    //This is found in schedule.ui.js
    populate_schedule_form();
  }
}

function filter_topics(search){
  var topic = $(select_topics_selector).find('li');
  topic.hide();
  topic.each(function(){
    //Get the text of the meeting title.
    var text = $(this).find('h6').text().toLowerCase();
    //Get the text the user typed into the search box.
    var search_text = (search.length > 0)? search.toLowerCase() : 0;
    //Hide the row.
    $(this).hide();
    //Check the value of the search.
    if(search_text == 0 || text.indexOf(search_text) != -1){
      //Show the rows that are available.
      $(this).show();
    }
  });

  //Find the rows inside of that meeting to load.
  var rows = $(identifier).find('#meeting_topics > tbody > tr');
  //Loop through each row.
  rows.each(function(){
    //Get the text of the meeting title.
    var text = $(this).find('h5').text().toLowerCase();
    //Get the text the user typed into the search box.
    var search_text = (search.length > 0)? search.toLowerCase() : 0;
    //Hide the row.
    $(this).hide();
    //Check the value of the search.
    if(search_text == 0 || text.indexOf(search_text) != -1){
      //Show the rows that are available.
      $(this).show();
    }
  });
}

function get_meeting_information(meeting){

  //Define a variable for the meeting attributes,
  //   these are in the html DOM meeting element.
  var meeting_attrs = Array();

  //Create the attribute names.
  meeting_attrs['publicid'] =  meeting_publicid_attr;
  meeting_attrs['name'] = 'meeting-name';
  meeting_attrs['description'] = 'meeting-description';
  meeting_attrs['duedate'] = 'meeting-duedate';
  meeting_attrs['duration'] = 'meeting-duration';
  meeting_attrs['startdate'] = 'meeting-startdate';
  meeting_attrs['starttime'] = 'meeting-starttime';
  meeting_attrs['ownername'] = 'meeting-ownername';
  meeting_attrs['topic_count'] = 'meeting-topic-count';
  meeting_attrs['topics'] = 'meeting-topics';
  meeting_attrs['category-order'] = 'meeting-category-order';

  //Get the classes for each meeting element.
  meeting_ids = Array();
  //Get the values for each meeting attribute.
  meeting_values = Array();

  //Loop through the meeting_attrs.
  for(key in meeting_attrs){
    //Show the meeting classes.
    meeting_ids[key] = '#'+meeting_attrs[key]
    var value = meeting.attr(meeting_attrs[key]);
    if(key == 'topics' && meeting_values['topic_count'] != 0 ||
      key == 'category-order'){
      value = $.parseJSON(value);
    }
    if(key == 'duration') value = value/60;
    //Get the meeting attribute values.
    meeting_values[key] = value;
  }

  var ret = Array();

  ret['meeting_attrs'] = meeting_attrs;
  ret['meeting_ids'] = meeting_ids;
  ret['meeting_values'] = meeting_values;

  return ret;

}

function get_topic_information(topic){

  topic_attrs = Array();
  topic_ids = Array();
  topic_values = Array();

  topic_attrs['publicid'] = topic_publicid_attr;
  topic_attrs['name'] = topic_name_attr;
  topic_attrs['description'] = topic_description_attr;
  topic_attrs['documents'] = topic_documents_attr;
  topic_attrs['meeting_publicid'] = topic_meeting_publicid_attr;

  //Loop through the meeting_attrs.
  for(key in topic_attrs){
    //Show the meeting classes.
    topic_ids[key] = '#'+topic_attrs[key];
    var value = topic.attr(topic_attrs[key]);
    if(key == 'documents' && value){
      value = value.slice(1,-1).replace(/\\/g,'');
      value = $.parseJSON(value);
    }else{
      value = unescape(value);
    }
    //Get the topic attribute values.
    topic_values[key] = value;
  }

  ret = Array();
  ret['topic_attrs'] = topic_attrs;
  ret['topic_ids'] = topic_ids;
  ret['topic_values'] = topic_values

  return ret;

}

function view_meeting(meeting){
  view_meeting_overload(meeting,true);
}

function view_meeting_overload(meeting,slide_screen){
  
  $('.black_overlay').show();
  
  var meeting_information = get_meeting_information(meeting);

  var meeting_attrs = meeting_information['meeting_attrs'];
  var meeting_ids = meeting_information['meeting_ids'];
  var meeting_values = meeting_information['meeting_values'];

  var _GET = getQueryParams(document.location.search);
  var topic_publicid = false;

  $('tbody[id=meeting-topics]').each(function(){
    var tbody = $(this);
    var table = tbody.closest('table');
    tbody.html('');
    table.hide();
  });

  $(meeting_form_header_selector).text('Add a Meeting');
  $(schedule_form_header_selector).text('Create the Schedule');

  $(edit_form_button_selector).attr('publicid',meeting_values['publicid']);
  $(delete_meeting_input_selector).val(meeting_values['publicid']);
  $(meeting_ids['name']).text('View '+meeting_values['name']);
  $(meeting_ids['description']).text(meeting_values['description']);
  var topics_html = Array(0);
  for(key in meeting_values['topics']){
    var topic = meeting_values['topics'][key];
    if(!topics_html[topic.category]){
      topics_html[topic.category] = "";
    }
    topic_attrs = 'class="'+scheduled_topic_in_meeting_class+'" ';
    topic_attrs+= topic_name_attr+'="'+escape(topic.name)+'" ';
    topic_attrs+= topic_publicid_attr+'="'+escape(topic.publicid)+'" ';
    topic_attrs+= topic_description_attr+'="'+escape(topic.description)+'" ';
    topic_attrs+= topic_meeting_publicid_attr+'="'+meeting_values['publicid']+'" ';
    topic_attrs+= topic_documents_attr+'=\''+JSON.stringify(topic.documents)+'\'';
    topics_html[topic.category] += "<tr "+topic_attrs+">";
    topics_html[topic.category] += "<td>"+topic.scheduleorder+"</td>";
    topics_html[topic.category] += "<td class=\"schedule-name\">"+topic.name+"</td>";
    topics_html[topic.category] += "<td class=\"schedule-presenter\">"+topic.presenter+"</td>";
    topics_html[topic.category] += "</tr>";
    if(_GET['topic'] && _GET['topic'] == topic.publicid){
      var current_topic_publicid = topic.publicid;
    }else{
      var current_topic_publicid = false;
    }
  }

  for(category in topics_html){
    var table_selector = "table[category-name='"+category+"']";

    category_order_num = 0
    for(key in meeting_values['category-order']){
      if(meeting_values['category-order'][key][0] == category.toLowerCase().replace(' ','-')){
        category_order_num = meeting_values['category-order'][key][1]
      }
    }

    $(table_selector).show()
                     .attr('category-order',category_order_num)
                     .find('tbody')
                     .html(topics_html[category]);
  }

  $("#wrap_documents table").sortElements(function(a, b){

    a_order_attr = $(a).attr('category-order');
    b_order_attr = $(b).attr('category-order');

    a_order = (a_order_attr) ? a_order_attr : 0;
    b_order = (b_order_attr) ? b_order_attr : 0;

    return a_order > b_order ? 1 : -1;
  });

  //$('table[category-name='++']').html(topics_html);
  //$(meeting_ids['topics']).html(topics_html);
  $(scheduled_topic_in_meeting_selector).hover(function(){
    show_topic($(this));
  });
  toggle_screen('view_meeting');
  adjust_schedule();

  if(current_topic_publicid){
    current_topic = $(meeting_ids['topics']).find("tr["+topic_publicid_attr+"='"+current_topic_publicid+"']");
  }else{
    current_topic = $("#wrap_documents table tbody tr:first");
  }
  show_topic(current_topic);

  var screen_height = $('.screen').height();

  $('#view_attendees').height(screen_height);

}

function adjust_schedule(){

  var schedule_wrapper_element = $(schedule_wrapper_selector);
  var schedule_wrapper_parent = schedule_wrapper_element;
  var height = $('body').height() - (90 + 41 + 40 + 60 + 50);
  var topic_table_height = $('#topic_table thead').height() + $("#topic_table tbody").height();
  $("#topic_table tfoot tr").height(height - topic_table_height);
}

function show_topic(topic){
  var _GET = getQueryParams(document.location.search);
  var topic_info = get_topic_information(topic);

  table_display_element = $('#document_table_display .table');

    //Get the topic attributes
    var topic_attrs = topic_info['topic_attrs'];
    var topic_ids = topic_info['topic_ids'];
    var topic_values = topic_info['topic_values'];

    if(topic_values['documents'] == 'undefined') return false;

    $(topic_ids['name']).text(topic_values['name']);

    var html_info = topic_values['description'];

    $(topic_ids['description']).html(html_info.replace(/\n/g, "<br />"));
    var documents_html = "";
    for(key in topic_values['documents']){
      
      var document_object = topic_values['documents'][key];
      documents_html += "<tr>";
      documents_html += '<td class="topic" onclick="window.location = \'/download/'+topic_values['publicid']+'/'+document_object.fileName+'\';">'+document_object.name+"</td>";
      documents_html += '<td><a href="/viewtopic/?publicid='+topic_values['publicid']+'&currentmeeting='+topic_values['meeting_publicid']+'">Feedback</a></td>';
      documents_html += "</tr>";
    }
    $(topic_ids['documents']).html(documents_html);

  if(topic_values['documents'].length > 0){
    table_display_element.show();
  }else{
    table_display_element.hide();
  }

}

function getQueryParams(qs) {
    qs = qs.split("+").join(" ");
    var params = {},
        tokens,
        re = /[?&]?([^=]+)=([^&]*)/g;
    while (tokens = re.exec(qs)) {
        params[decodeURIComponent(tokens[1])]
            = decodeURIComponent(tokens[2]);
    }
    return params;
}

function create_meeting_schedule(){
  var items = $(create_schedule_droppable_selector);
  var schedule = '';
  var schedule_input = $(schedule_input_selector);
  items.each(function(){
    var item = $(this);
    var publicid = item.attr('publicid');
    schedule += publicid+',';
  });
  schedule_input.val(schedule);
}

function identify_meeting_form(form_name, value){
  var elem = $(meeting_form_identity_selector)
  elem.attr('name',form_name);
  if(!value){
    value = "";
  }
  elem.val(value);
}
function populate_topics_selector(){
  $(select_topics_selector).html("");
  $(available_topics_droppable_selector).each(function(){
    var droppable = $(this);
    var clone = droppable.clone();
    clone.appendTo(select_topics_selector);
  });
}
function fill_meeting_form(meeting){
  if(meeting){
    var meeting_info = get_meeting_information(meeting);
    var edit_meeting_header_value = 'Edit the Meeting';
    var edit_schedule_header_value = 'Edit the Schedule';
    var meeting_submit_button_value = "Update Meeting";
    var screen_id = 'edit_meeting';
    var form_input_value = meeting_info['meeting_values']['publicid'];
    var topics = meeting_info['meeting_values']['topics'];
    var category_order = meeting_info['meeting_values']['category-order'];

    var schedule_grid_html = "";
    for(key in topics){
      var topic = topics[key];
      var attributes = 'class="droppable border-box" ';
      attributes += 'duration="'+topic.duration+'" ';
      attributes += 'publicid="'+topic.publicid+'" ';
      attributes += 'style="height: '+(topic.presentationlength * 2)+'px; position:relative;"';

      schedule_grid_html+="<li "+attributes+">";
      schedule_grid_html+="<h6>"+topic.name+"</h6>";
      schedule_grid_html+="</li>";
    }

    for(key in category_order){
      var category_name = category_order[key][0];
      var category_order_value = category_order[key][1];

      $('div[category-row-category-name='+category_name+']').attr('category-order',category_order_value);
    }

    $('.category-row').sortElements(function(a, b){
      return $(a).attr('category-order') > $(b).attr('category-order') ? 1 : -1;
    });

  }else{
    var meeting_info = false;
    var edit_meeting_header_value = 'Add a Meeting';
    var edit_schedule_header_value = 'Create the Schedule';
    var meeting_submit_button_value = "Create Meeting";
    var screen_id = 'add_meeting';
    var form_input_value = false;
    var schedule_grid_html = false;
  }
  
  identify_meeting_form(screen_id, form_input_value);

  $(meeting_submit_button_selector).val(meeting_submit_button_value);

  if(schedule_grid_html){
    $(schedule_grid_selector).html(schedule_grid_html);
   }else{
    $(create_schedule_droppable_selector).each(function(){
      var droppable = $(this);
      var clone = droppable.clone();
      droppable.remove();
    });
  }

  populate_topics_selector();

  $(meeting_form_header_selector).text(edit_meeting_header_value);
  $(schedule_form_header_selector).text(edit_schedule_header_value);

  $(meeting_form_table_selector)
  .find('input[type="text"],textarea').each(function(){
    var field = $(this);
    var name = field.attr('name');

    if(meeting){
      var value = meeting_info['meeting_values'][name];
      if(name == 'starttime'){
        hour = value.substr(0,2);
        minute = value.substr(3,2);
        if(hour < 12 ){
          if(hour == 0 ) hour = 12;
          period = "am";
        }else{
          if(hour != 12 ) hour = hour - 12; 
          period = "pm";
        }
        value = hour+':'+minute+period;
      }
      field.val(value);
    }else{
      field.val('');
    }
  });  
}

function edit_meeting(button){
  var publicid = button.attr('publicid');
  var meeting = $('li['+meeting_publicid_attr+'="'+publicid+'"]');

  $('#submit_meeting_info_button').show();
  $('#edit_schedule_button').hide();

  show_screen(meeting_form_id, false);
  
  fill_meeting_form(meeting);
  
  load_meeting_schedule(meeting);
  
  // /create_meeting_schedule();
}

function edit_schedule(button){

  var publicid = button.attr('publicid');
  var meeting = $('li['+meeting_publicid_attr+'="'+publicid+'"]');
  show_screen(schedule_form_id, false);
  
  fill_meeting_form(meeting);

  load_meeting_schedule(meeting);

  window_loop();

  // /create_meeting_schedule();

}

function hide_meeting(){
  $(screen_selector).hide();
  $('.black_overlay').hide();
}

$(function(){
  window_hash = window.location.hash;
  if(window_hash){
    publicid = window_hash.replace('#','')
    meeting = $('li['+meeting_publicid_attr+'="'+publicid+'"]');
    view_meeting_overload(meeting,false);
  }

  $('#nextmeeting').click(function(){
    var meeting = $(this);
    var publicid = meeting.attr('publicid');
    var year = meeting.attr('starting-year');
    var month = meeting.attr('starting-month');
    window.location = "/viewmeetings/?month="+month+"&year="+year+"#"+publicid;
  });

  $(window).resize(function(){
    //Start the window loop.
    window_loop();
  });
  window_loop();
  $(document).keyup(function(e) {
    if (e.keyCode == 27) {
      remove_form_add_meeting();
      hide_meeting();
    }
  }).click(function(e){
    var target = e.target;
    var exists = false;
    classlist = target.classList;
    for (var k in classlist){
      classname = classlist[k]
      if(classname == 'cell_wrapper') exists =true
    }
    element = $(target).parents('.cell_wrapper');
    if(!exists && element.length == 0){
      remove_form_add_meeting();
    }
  });
  $('.meeting-item').click(function(e){
    view_meeting($(this));
    window_loop();
    e.stopPropagation();
  });
  //Click event for the cell info.
  cell_info_click();
  //Add in the row selector.
  $(calendar_rows_selector+" th").parent().height(40).css('border','0');
  var calendar_cells = $(calendar_cell_wrapper_selector);
  make_cell_background(calendar_cells)
  calendar_cells.click(function(){
    var calendar_day_form_element = $(calendar_day_form_selector);
    if($(meeting_form_selector).is(':visible')) return true
    var cell = $(this);
    if(!cell.hasClass(opened_cell_class)){
      close_opened_cell();
    }
    var cell_td = cell.closest('td');
    var cell_forms = cell.find('.cell_forms');
    var cell_form_count = cell_forms.find('form');
    var cell_date = cell_td.attr('date-value');
    var cut_off_cell_date = cell_td.attr('cut-off-date-value');
    var cell_textual_date = cell_td.attr('date-textual');

    if(!cell_td.hasClass('noday') && cell_form_count.length == 0){
      make_cell_background(calendar_cells);
      cell.css({'background':cell_selected_bgcolor});
      $(calendar_day_form_copy_selector).remove();
      var calendar_form_clone = $(calendar_day_form_selector+':first').clone();
      cell_forms.append(calendar_form_clone);
      var calendar_form = cell_forms.find(calendar_day_form_selector);
      calendar_form.find('.item-wrap .date').html(cell_textual_date);
      calendar_form.find('input[name="duedate"]').val(cut_off_cell_date);
      calendar_form.find('input[name="startdate"]').val(cell_date);
      calendar_form.addClass(calendar_day_form_copy_class);
      calendar_form.show().css({
        'z-index':'3000',
        'position': 'absolute',
        'top':-160,
        'left':-60
      });
    }
    cell.find('.close-calendar-day').click(function(e){
      remove_form_add_meeting();
      e.stopPropagation();
    });
    $(hide_cell_info_selector).removeClass(hide_cell_info_class);
  });

  $('.scale').each(function(){
    var hours = 24;
    var half_hours = hours * 2;

    var scale = $(this);

    for(i = 0; i < half_hours; i++){
      mod = i % 2;
      if(mod == 0){

        var classname = 'hour';
        var hour = i/2;

        if(hour == 0){
          hour = 12;
        }
        
        if(hour >= 13){
          hour = hour - 12;
        }

        hour = hour +"<sup>00</sup>";

        if(i == 0){
          hour = hour + '<br><small>am</small>';
        }else if(i == 24){
          hour = hour + '<br><small>pm</small>';
        }
        
       }else{
        var classname = 'half_hour';
        var hour = "";
      }
      
      var hour_marker = i/2;

      scale.append('<div hour-marker="'+hour+'" class="scale-item '+classname+' border-box">'+hour+'</div>');

    }

    var this_height = $(this).parent()[0].scrollHeight;
    var this_width = $(this).parent().width() - $(this).width() - 16;
    $(schedule_grid_selector).height('100%')
                         .width('92%');

  });
});

var duration_input = $('#id_duration');

if(duration_input.length > 0){
  duration_input.closest('td').append('hrs');
}

function adjust_category_row_height(){
  $('.category-row').each(function(){
    var category_row = $(this);
    var topics_wrapper = category_row.find('.category');
    var category_schedule = category_row.find('.category-schedule');
    var category_description = category_row.find('.category-description');

    var topics_wrapper_height = topics_wrapper.height();
    var category_schedule_height = category_schedule.height();
    var category_description_height = category_description.height();

    var elem_height = (topics_wrapper_height > category_schedule_height) ? topics_wrapper_height : category_schedule_height;

    topics_wrapper.height(elem_height);
    category_schedule.height(elem_height);

    category_row.height(elem_height + 40);
  });
}