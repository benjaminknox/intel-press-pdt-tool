var background_gradient_class = 'background-gradient';

var view_documents_wrapper_id = 'view_documents_wrapper';
var view_documents_wrapper_selector = '#'+view_documents_wrapper_id;

var view_topics_sidebar_id = 'view_topics_sidebar';
var view_topics_sidebar_selector = '#'+view_topics_sidebar_id;

var search_results_id = 'search_results';
var search_results_selector = '#'+search_results_id;

var search_results_table_class = 'search_results_table';
var search_results_table_selector = '.'+search_results_table_class;
var search_results_table_row_selector = search_results_table_selector+' tr';

var search_results_topic_class = 'topic'
var search_results_topic_selector = '.'+search_results_topic_class;

var topic_category_name_class = 'topic-category';
var topic_category_name_selector = '.'+topic_category_name_class;
var topic_category_attr = 'topic-category';

var search_topics_input_id = 'search_topics_input';
var search_topics_input_selector = '#'+search_topics_input_id;

var live_document_item_class = 'live_document_item';
var live_document_item_selector = '.'+live_document_item_class;

var documents_scroller_right_edge;
var documents_scroller_width;
var documents_scroller_left_edge;
var last_document_right_position;
var screen_center;
var last_document_edge_distance_from_center;

var html_body_selector = 'HTML, BODY';

var isIPad;

/* This function resizes the div when the page reloads.
*/function window_resize(){

  var win = $(window);
  var html_body = $(html_body_selector);

  var winHeight = win.height();
  var winWidth = win.width();

  var minHeight = 600;
  var minWidth = 700;

  if(winHeight < minHeight){
    $(html_body_selector).height(minHeight);
  }else{
    $(html_body_selector).height('100%');
  }

  if(winWidth <= minWidth){
    html_body.width(minWidth);
  }else{
    html_body.width(winWidth);
  }

  var searchForm = $('#search_form');
  var searchFormWidth = searchForm.width();

  adjust_document_size();

  var headerHeight = $('#header').height();
  
  searchForm.find('#search_topics_input').width(searchFormWidth - 80);

  var searchFormHeight = searchForm.height();

  var displayHeight = winHeight - headerHeight;

  $('.shadow').height(displayHeight).css({'top':headerHeight});

  $(view_documents_wrapper_selector+','+view_topics_sidebar_selector).height(displayHeight);

  $(search_results_selector).height(displayHeight - searchFormHeight);

  $('body').addClass(background_gradient_class);

  //var winHeight = $(window).height();
}

/* Color the odd row of each table.
*/function search_results_coloring(){
  var light_hex ='#7d7e7d';
  var dark_hex ='#777777';
  var i = 0;
  $(search_results_table_row_selector).each(function(){
    var row = $(this);
    if(i % 2 == 1){
      var background = dark_hex;
    }else{
      var background = light_hex;
    }
    row.css({'background':background});
    if(row.is(':visible')){
      i++;
    }
  });
}

/* This searches the topics.
*/function search_topics(input){
  var search_value = input.val();
  var search_text = (search_value.length != 0) ? search_value : 0;

  if(search_text){
    $(search_results_topic_selector).each(function(){
      var topic = $(this);
      var value = topic.text();
      if(value.indexOf(search_text) != -1 && search_value != 0){
        topic.show();
      }else{
        topic.hide();
      }
    })
  }else{
    $(search_results_table_row_selector).show();
  }
  
  search_results_coloring();
}

/* When the window gets resized.
*/$(window).resize(function(){
  //Start the window loop.
  window_resize();
});

$(search_results_topic_selector).click(function(){

  $(live_document_item_selector).remove();

  var topic = $(this);
  var doc = topic.attr('documents');
  var documents = $.parseJSON(doc);
  var center_documents = $('#center_documents');

  var view_document_width = 0;

  for(key in documents){

    var doc = documents[key];
    
    var publicid = doc['publicid'];
    var name = doc['name'];
    var image_url = doc['image_url'];

    if(isIpad){
      var initialElement = '#init-document-ipad';
      var extra_width = 40;
    }else{
      var initialElement = '#init-document';
      var extra_width = 0;
    }

    var initDoc = $(initialElement);

    var docWidth = initDoc.width() + extra_width;

    var document_object = initDoc.clone();

    view_document_width += docWidth;

    document_object.find('.document_label').append(name);

    document_object.removeAttr('id')
                   .addClass(live_document_item_class)
                   .appendTo(center_documents);

  }

  documents_scroller_width = view_document_width;

  $(view_documents_wrapper).width(view_document_width)
                           .css({'left':screen_center});
  
  adjust_document_size();

});

/* Open the categories.
*/$(topic_category_name_selector).click(function(){
  var row = $(this);
  var category = row.attr('category-name');
  var topics = $('tr['+topic_category_attr+'="'+category+'"]');
  topics.toggle();
  search_results_coloring();  
});

$(search_topics_input_selector).keyup(function(){
  search_topics($(this));
});

function get_screen_center(){
      winWidth = $(window).width();
      screen_center = winWidth/2;
}

function adjust_document_size(){

  if(!isIpad){
  
    get_screen_center();

    var documents = $(live_document_item_selector).find('.document');
    var documents_count = documents.length;
    var view_documents_width = 0;

    documents.each(function(){
      var doc = $(this);
      var doc_position = doc.offset();
      
      var screenWidth = winWidth / 2;

      var from_center = -1*(Math.abs(doc_position.left - screen_center  ) - screenWidth);

      var mat = (Math.abs(3 + (from_center*from_center)/4))/350;
      var width = mat * .786;
      var height = mat;
      var margin_top = (mat * -0.3 / 2) + 140;
      var margin_left = width / -2;
      var zIndex = Math.ceil(height);
      var parentWidth = width+50;

      doc.width(width)
         .height(height)
         .css({
          'margin-top': margin_top+'px',
          'margin-left':margin_left+'px'
         })
         .zIndex(zIndex);

       doc.parent().width(parentWidth);

       view_documents_width += parentWidth;

    });

    $(view_documents_wrapper_selector).width(view_documents_width + 100);

  }
}

function get_scroller_dimensions(){

  var scroller = $(view_documents_wrapper_selector);
  var last_document_item = $('.live_document_item:last');
  var last_document_width = last_document_item.width();
  var last_document_left = last_document_item.offset().left;
  var last_document_right = last_document_left + last_document_width;
  last_document_edge_distance_from_center = (screen_center - documents_scroller_right_edge);

  documents_scroller_left_edge = scroller.offset().left;
  documents_scroller_width = scroller.width();
  documents_scroller_right_edge = documents_scroller_left_edge + documents_scroller_width;

}

function window_loop(){
  
    if($(view_documents_wrapper_selector).is(':animated')){
      adjust_document_size();
      get_scroller_dimensions();
    }

    var t = setTimeout('window_loop()', .005)
}

/* This is an event on the page.
*/$(function(){

  isIpad = navigator.userAgent.match(/iPad/i) != null;

  window_loop();

  adjust_document_size();

  search_results_coloring();
  window_resize();
  $(view_documents_wrapper_selector).draggable({
    axis:'x',
    drag:function(event,ui){
      get_screen_center();
      get_scroller_dimensions();
      if(event.pageX >= $(window).width() - 100 || event.pageX <= 100){
        return false;
      }
      adjust_document_size();
    },
    stop:function(event,ui){
     $(this).css({'cursor':'inherit'});
     $(html_body_selector).css({'overflow-x':'hidden'});
     if(documents_scroller_left_edge > screen_center){
      $(this).animate({
          left:screen_center - 100
        }, 100);
     }
    }
  });
});