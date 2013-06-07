//Set the window properties.
var win = $(window);
var winHeight, winWidth;
var minWinHeight = 480;
var minWinWidth = 1024;
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
//This is a variable for the header height.
var header_height;
//This is a selector for the content element.
var content_id = 'document_content';
var content_selector = '#'+content_id;
var content_element;
//These are document scroller elements.
var document_scroller_wrapper_id = "document_scroller_wrapper";
var document_scroller_wrapper_selector = "#"+document_scroller_wrapper_id;
var document_scroller_element, document_scroller_width;
//This is an individual document.
var document_class = "document";
var document_selector = "."+document_class;
var document_height,document_width,document_element,document_margin_left;
var screen_selector = '.screen';

var comment_form_class = 'comment_form';
var comment_form_selector = '.'+comment_form_class;

var document_upload_form_class = 'document_upload_form';
var document_upload_form_selector = '.'+document_upload_form_class;

var add_document_form_id = 'add_document_form';
var add_document_form_selector = '#'+add_document_form_id;

var update_document_form_class = 'update_document_form';
var update_document_form_selector = '.'+update_document_form_class;

var topic_display_id = 'topic_display';
var topic_display_selector = '#'+topic_display_id

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
    $(screen_selector).slideUp();
  }
}).click(function(e){
    var target = e.target;
    var target_element = $(target);
    
    var comment_form = false;
    var add_document_form = false;
    var update_document_form = false;

    var classlist = target.classList;

    for (var k in classlist){
      classname = classlist[k]
      
      if(target_element.closest(comment_form_selector).length > 0 ||
      classname == 'feedback' ||
      classname == 'reply_button'){
          comment_form = true;
      }
      
      if( target_element.closest(add_document_form_selector).length > 0 || 
        classname == 'add-document'){
          add_document_form = true;
      }
      
      if( target_element.closest(update_document_form_selector).length > 0 || 
        classname == 'update-document'){
          update_document_form = true;
      }
    }

    if(!comment_form) $(comment_form_selector).hide();
    if(!add_document_form) $(add_document_form_selector).hide();
    if(!update_document_form) $(update_document_form_selector).hide();

  });

function verify_change_presentation_length(form){
  var c = confirm('Are you sure? Your topic will be removed from the meeting it is currently in, and will be added to the next meeting with an available slot.');
  if(c){
    form.submit();
  }
}

function add_document(){
  $(add_document_form_selector).show();
}

function update_document(button){
  $(document_upload_form_selector).hide();
  var document_element = button.closest(document_selector);
  var update_document_element = document_element.find(document_upload_form_selector);

  update_document_element.show();
}

function delete_document(button){
  var document_element = button.closest(document_selector);
  var form = document_element.find('.delete_document_form');

  form.submit();

}

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
  
  //Set the content element.
  content_element = $(content_selector);
  //get the header height.
  header_height = (navbar_element.height() + infobar_element.height());

  //Get the document scroller width.
  document_scroller_element = $(document_scroller_wrapper_selector);
  document_scroller_width = document_scroller_element.width();

  //Get the document element and width.
  document_element = $(document_selector);

  //Going to create a perspective, it will be 75% of 
  //    the width of document_scroller for the website.
  document_height = document_scroller_width - (document_scroller_width * .10);
  document_width = document_scroller_width * .75;
  document_margin_left = document_scroller_width * .115;

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
  content_height = html_bodyElement.height() - header_height - 3;
  //Set the content_element height.
  content_element.height(content_height);

  var feedback_scroller_element =  $('#document_feedback_scroller');
  var document_scroller_element =  $('#document_scroller');
  var topic_display_element =  $(topic_display_selector);

  var scroller_height = content_height - 42;

  feedback_scroller_element.height(scroller_height);
  feedback_scroller_element.find('topic_comment_wrapper').height(scroller_height);

  document_scroller_element.height(scroller_height);

  if(winWidth < 1386){
    var feedback_scroller_element_width = '25%';
    var document_scroller_element_width = '25%';
    var topic_display_width = '48.7%';
    var topic_display_margin = '51%';
  }else{
    var feedback_scroller_element_width = '17.8%';
    var document_scroller_element_width = '15%';
    var topic_display_width = '65.8%';
    var topic_display_margin = '33.8%';
  }
  feedback_scroller_element.parent().width(feedback_scroller_element_width);
  document_scroller_element.parent().width(document_scroller_element_width);
  topic_display_element.width(topic_display_width).css({'margin-left':topic_display_margin});
}