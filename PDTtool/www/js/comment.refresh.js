$(document).ready(function(){
  get_comments();
});

function get_comments(){
  var topic_publicid = $('#topic_publicid').val();
  var csrfmiddlewaretoken = $('#csrftokenvalue').val();
  var url = "/long_poller_topic_comments/?topic_publicid="+topic_publicid+"&publicid="+topic_publicid;//"/topic_comments/?publicid="+topic_publicid;
  var data = {publicid:topic_publicid,topic_publicid:topic_publicid,csrfmiddlewaretoken:csrfmiddlewaretoken}
  var success = function(data){
    if(data != "9"){
       $("#topic_comment_wrapper").html(data);
    }
    get_comments();
  }
  var dataType = "text";
  $.ajax({
    type: "POST",
    url: url,
    data: data,
    success: success,
    dataType: dataType
  });
}