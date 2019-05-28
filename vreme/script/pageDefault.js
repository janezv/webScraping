





//making links on the pictures   
function newHome(){
  window.location='../vreme/index.php';
}
function newWindow(){
  window.location='../vreme/opozorila.php';
}
function winMeritve(){
  window.location='../vreme/sneg.php';
}
function winZgodovinaT(){
  window.location='../vreme/temper.php';
}




//making sticky effect on header and over header
window.onscroll = function() {myFunction()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myFunction() {
  var x = screen.width;
  //disable sticky effect for the screen that are smaller then 992px
  if(x > 992 ){
    if (window.pageYOffset >= sticky) {
      header.classList.add("sticky");
    } else {
      header.classList.remove("sticky");
    }
  }
}
