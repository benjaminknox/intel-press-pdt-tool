//Set the window properties.
var win = $(window);
var winHeight, winWidth;
var minWinHeight = 480;
var minWinWidth = 640;
//This is a selector for the document
//    HTML and BODY tags.
var html_bodySelector = 'HTML,BODY';
var html_bodyElement;
//These are selectors for the navigation
//    and info bar at the top of the script.
var navbar_selector = '#navbar';
var navbar_element;
var infobar_selector = '#infobar';
var infobar_element;
//This is a selector for the toolbar, under
//    the navbar and the infobar.
var topic_toolbar_id = 'topic_toolbar';
var topic_toolbar_selector = '#'+topic_toolbar_id;
var topic_toolbar_element;
//This is a variable for the header height.
var header_height;
//This is a selector for the content element.
var content_id = 'topic_content';
var content_selector = '#'+content_id;
var content_element;
//This is a variable for the height of
//  the content area.
var content_height;
//This is a selector for the sidebar, on the 
//    left of the screen.
var topic_sidebar_id = 'topic_sidebar'
var topic_sidebar_selector = '#'+topic_sidebar_id;
var topic_sidebar_element;
//This is a selector for the elements in 
//  the topics_list table.
var topics_list_id = 'list';
var topics_list_selector = '#'+topics_list_id;
var topics_list_tr_selector = topics_list_selector+' tbody tr';
var topics_list_thead_selector = topics_list_selector+' thead';
var topic_name_column_selector =  topics_list_selector+' .topic_name';
var topic_owner_column_selector =  topics_list_selector+' .topic_owner';
var topic_category_column_selector =  topics_list_selector+' .topic_category_col';
var topic_status_column_selector = topics_list_selector+' .topic_stats';
var topics_list_element;
var topics_list_thead_element;
var topic_name_column_element;
var topic_owner_column_element;
var topic_category_column_element;
var topic_status_column_element;
var topics_list_width;
//Get the selected topics.
var topic_selected_class = 'topic-selected';
var topic_selected_selector = '.'+topic_selected_class;

var screen_selector = '.screen';

//These are selectors for 
$(function(){
  //Resize the window
  window_resize();
});

//When a window is resized run the function.
win.resize(function(){
  //Resize the window.
  window_resize();
});

$(document).keyup(function(e) {
  if (e.keyCode == 27) {
    $(screen_selector).hide();
  }
})

function window_resize(){
  //Set the window height.
  winHeight = win.height();
  //Set the window width.
  winWidth = win.width();
  //Set the html_bodyElement.
  html_bodyElement = $(html_bodySelector);
  //Set the navbar element.
  navbar_element = $(navbar_selector);
  //Set the infobar element.
  infobar_element = $(infobar_selector);
  //Set the topic_toolbar element.
  topic_toolbar_element = $(topic_toolbar_selector);
  //Set the topic_sidebar element.
  topic_sidebar_element = $(topic_sidebar_selector);
  //Set the topics_list width
  topics_list_element = $(topics_list_selector);
  topics_list_width = topics_list_element.width();
  //Set the topics_list head element.
  topics_list_thead_element = $(topics_list_thead_selector);
  topic_name_column_element = $(topic_name_column_selector);
  topic_owner_column_element = $(topic_owner_column_selector);
  topic_category_column_element = $(topic_category_column_selector);
  topic_status_column_element = $(topic_status_column_selector);

  //Set the content element.
  content_element = $(content_selector);
  //get the header height.
  header_height = (navbar_element.height() + infobar_element.height() + topic_toolbar_element.height());

  //Check the minimum height.
  if(winHeight < minWinHeight){
    html_bodyElement.height(minWinHeight);
    winHeight = minWinHeight;
  }else{
    html_bodyElement.height('100%');
  }
  //Check the minimum width.
  if(winWidth < minWinWidth){
    html_bodyElement.width(minWinWidth);
    winWidth = minWinWidth;
  }else{
    html_bodyElement.width('100%');
  }

  //Get the content height.
  content_height = html_bodyElement.height() - header_height - 23;

  //Set the content_element height.
  content_element.height(content_height);
  
  topics_list_thead_element.width(topics_list_width);

  topic_name_column_element.width(topics_list_width * .6);
  topic_owner_column_element.width(topics_list_width * .15);
  topic_category_column_element.width(topics_list_width * .10);
  topic_status_column_element.width(topics_list_width * .15);

}

function select_category(element){
  var category = element.attr('category');
  if(category == 'all'){
    var selector = topics_list_tr_selector;
   }else if(category == 'mytopics'){
    var selector = "tr[owner=true]";
   }else{
    var selector = "tr[category='"+category+"']";
  }
  $(topics_list_tr_selector).removeClass('search-not-found')
                            .addClass('topic-not-selected');
  $(selector).addClass(topic_selected_selector)
             .removeClass('topic-not-selected');
  $('#search_topics').val('');
}

function edit_form(){
  $(screen_selector).show();
  $(screen_selector+' h3.page-title').text('Add Topic');
}

function search_topics(input){
  var search = input.val();
  //Get the text the user typed into the search box.
  var search_text = (search.length > 0) ? search.toLowerCase() : 0
  var topics = $(topic_selected_selector);

  topics.each(function(){
    var text = $(this).text().toLowerCase();;
    //Hide the row.
    $(this).addClass('search-not-found');
    //Check the value of the search.
    if(search_text == 0 || text.indexOf(search_text) != -1){
      //Show the rows that are available.
      $(this).removeClass('search-not-found');
    }
  });
}
/*
$('#list thead .topic_name').click(function(){

  window.topic_value = (window.topic_value) ? false : true;

  $(".topic").sortElements(function(a, b){
    var a_value = $(a).find('.topic_name').text();
    var b_value = $(b).find('.topic_name').text();
    if(window.topic_value){
        return a_value > b_value ? 1 : -1;
    }else{
        return a_value < b_value ? 1 : -1;
    }
  });
});*/

$('#list thead th').each(function(){

  var class_name = $(this).attr('class');

  if(!window.topic_value){
    window.topic_value = Array();
  }

  window.topic_value[class_name] = true;

  $(this).click(function(){

    $('.arrow').removeClass('arrow-up').removeClass('arrow-down');

    window.topic_value[class_name] = (window.topic_value[class_name]) ? false : true;

    $(".topic").sortElements(function(a, b){
      var a_value = $(a).find('.'+class_name).text();
      var b_value = $(b).find('.'+class_name).text();
      if(window.topic_value[class_name]){
          return a_value > b_value ? 1 : -1;
      }else{
          return a_value < b_value ? 1 : -1;
      }
    });

    if(window.topic_value[class_name]){
      $(this).find('.arrow').addClass('arrow-up');
    }else{
      $(this).find('.arrow').addClass('arrow-down');
    }

  });

});