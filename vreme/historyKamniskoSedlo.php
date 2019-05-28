<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="../vreme/Desigen/zgodovina.css3"><!--barve oblikae okna-->
    <link rel="stylesheet" type="text/css" href="../vreme/Desigen/table.css3"> <!--lastnosti in animacija glavne tabele-->
    <script>
        function showPicture(ime){
                var img=ime.src;              
                window.open("../vreme/showOnePicture.php?img="+img,"_blank", "toolbar=no, scrollbars=yes, resizable=yes, width=960, height=600");
       
        }
        function home(){
                window.location='../vreme/index.php';
        }
    </script>
</head>
<body>
    <div id="head" style="text-align:center">
        <table style="width: 100%">
        <tr>
        <td><div style="cursor:pointer; float: left"><img src="../vreme/Desigen/Home.png" onclick="home()" onmouseover="this.width='60'" onmouseout="this.width='50'"></div>
            </td><td><h1>Slike kredarica</h></td>
            </tr>
            </table>
        </div>
        <br>
    </body>
</html>

<?php
//google: how can i display all picture in folder
//link: http://stackoverflow.com/questions/11903289/pull-all-images-from-a-specified-directory-and-then-display-them

function showAllPictures(){
  session_start();
  $files = glob("../vreme/onlinePictures/historyKamniskoSedlo/*.*");
  $st=count($files); //število vseh filov

  for ($st; 0 <= $st; $st--)
    {
        $image = $files[$st];
        $_SESSION['images'][] = $image;
        $fileEtension = array('jpg','png');
        $ext = pathinfo($image, PATHINFO_EXTENSION);
        if (in_array($ext, $fileEtension)) {   
            echo "<img id='$st' src='$image' height='270' width='480' onclick='showPicture(this)' style='cursor:pointer; margin-top:10'> &nbsp &nbsp";
        } 
    }
    
}

showAllPictures();

//slide show
//    google:  How to pass an array using PHP & Ajax to Javascript?
//      http://stackoverflow.com/questions/9001526/send-array-with-ajax-to-php-script

?>