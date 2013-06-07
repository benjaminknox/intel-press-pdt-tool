var iOS = ( navigator.userAgent.match(/(iPad|iPhone|iPod)/g) ? true : false );


if(iOS){
  $('.ios').show();
  $('.desktop').hide();
 }else{
  $('.ios').hide();
  $('.desktop').show();
}