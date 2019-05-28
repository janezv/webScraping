    

//on the begining set all picture in the <nav> to proper value
$(document).ready(function(){
//make picture in nav to animate
$('#kr').mouseenter(function(){
    $('#kr').css({"height":"90px","cursor":"pointer"});
});
$('#kr').mouseleave(function(){
    $('#kr').css({"height":"60px","cursor":"default"});
});
$('#lj').mouseenter(function(){
    $('#lj').css({"height":"90px","cursor":"pointer"});
});
$('#lj').mouseleave(function(){
    $('#lj').css({"height":"60px","cursor":"default"});
});
$('#kp').mouseenter(function(){
    $('#kp').css({"height":"90px","cursor":"pointer"});
});
$('#kp').mouseleave(function(){
    $('#kp').css({"height":"60px","cursor":"default"});
});
})