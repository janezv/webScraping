<?php
session_start();

function odg(){
    $x=$_POST['p1'];
    $x=$_POST['p1'];
    $y=explode("/",$x);
    $imgSrc = '../'.$y[3].'/'.$y[4].'/'.$y[5].'/'.$y[6];

    
    $files = glob("../vreme/onlinePictures/historyKredarica/*.*");
    $max=sizeof($files); //število vseh filov
    for($i = 0; $i < $max;$i++)
    {
        if($i<1)$i=1;
        if($imgSrc==$files[$i]) echo $files[$i-1];
    }
    //echo $imgSrc;
  //  $key = array_search($x, $_SESSION['images']); // $key = 2;
}
odg();

?>