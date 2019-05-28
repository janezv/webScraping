    

//on the begining set all picture in the <nav> to proper value
$(document).ready(function(){
        $('.imgNav').css({"width":"100px","height":"90px","margin-left":"60px"});


//make picture in nav to animate
$('#img1').mouseenter(function(){
    $("#img1").css({"width":"150px","height":"120px"});
});
$('#img2').mouseenter(function(){
    $("#img2").css({"width":"150px","height":"120px"});
});
$('#img3').mouseenter(function(){
    $("#img3").css({"width":"150px","height":"120px"});
});
$('#img1').mouseleave(function(){
    $("#img1").css({"width":"100px","height":"90px"});
});
$('#img2').mouseleave(function(){
    $('#img2').css({"width":"100px","height":"90px"});
});
$('#img3').mouseleave(function(){
    $('#img3').css({"width":"100px","height":"90px"});
});
})