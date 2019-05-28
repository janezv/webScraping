<?php
//zbrisi variable v session
session_start();
session_unset();
session_destroy();
//določi današnji dan
$now = time();
$nowUSA=date("Y-m-d",$now);
$clock=date("H:i",$now);

//zapisi IP obiskovalca
$ip=$_SERVER['REMOTE_ADDR'];
//zapisi IP in datum obiska v mysql
$conn = mysqli_connect("localhost", "webScreping", "webScreping", "webScraping");   //$servername, $username, $password, $dbname
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
//enable UNICODE character
mysqli_query($conn,"SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'");
$sql="INSERT INTO obisk (obisk.dan, obisk.IP, obisk.ura) VALUES('$nowUSA','$ip','$clock')";
mysqli_query($conn, $sql);

?>
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="../vreme/Desigen/main.css">
</head>    
<body>
  <div class="top-container">
    <h1>Interaktivna stran za zbiranje podatkov iz interneta</h1>
  </div>
  <div class="header" id="myHeader">
  <ul>
     <li onclick="newHome()"><a href="#news">Domov</a></li>
     <li onclick="winZgodovinaT()"><a href="#news">Seznam zgodovine temperature</a></li>
     <li onclick="winMeritve()"><a href="#contact">Seznam zgodovine snežne oddeje</a></li>
     <li onclick="newWindow()"><a href="#about">Seznam zgodovine izdanih opozoril</a></li>
  </ul>
  </div>
  <div class="containter">

     <div class="left">
         <img id="Kredarica" class="imgOnline" src="../vreme/onlinePictures/Kredarica.jpg" title="Prikaz Kredarice skozi dni" onclick="window.location='../vreme/historyKredarica.php'">
         <img class="imgOnline" src="../vreme/onlinePictures/KamniskoSedlo.jpg">
         <img class="imgOnline" src="../vreme/onlinePictures/SmarnaGora.jpg">
     </div>

     <div class="map">
         <div id="mapCanvas" style="height:600px; width:700px"></div>
     </div>
     
     <div class="right"> 
         <img class="imgOnline" src="../vreme/onlinePictures/Grintovec.jpg">
         <img class="imgOnline" src="../vreme/onlinePictures/Zavizan.jpg">
         <!--<a href="https://drive.google.com/open?id=0B4gnSJAOOtlgSjJyX2pNZTZlS3M">Android kalkulator</a></td></tr>
         <a href="https://drive.google.com/open?id=0B4gnSJAOOtlgZDdqLUFxU3hKVjA">Android kalkulator energetske vrednosti lesa</a></td></tr>-->
     </div>
 
   </div>
    <script>
      var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('mapCanvas'), {
          center: {lat: 46.056609, lng: 14.95},
          zoom: 8,
          mapTypeId: 'terrain'
        });  
	// Make a points
        var pKredarica = {lat: 46.378864, lng: 13.848783};
        var pKamnisko = {lat: 46.359201, lng: 14.597349};
        var pSmarna = {lat: 46.129736, lng: 14.463805};

        //info Windows
	var contetnKredarica = "<div>Kredarice 2515m<br></div>"+
           "<div><a href='../vreme/historyKredarica.php'><img id='Kredarica' src='../vreme/onlinePictures/Kredarica.jpg'  width='105' height='75'></a></div>";

        var contetnKamnisko = "<div>Kamniško sedlo 1903m<br></div>"+
           "<div><img id='Kredarica' src='../vreme/onlinePictures/KamniskoSedlo.jpg'  width='105' height='75'></div>";

        var contetnSmarna = "<div>Šmarna gora 669m<br></div>"+
           "<div><img id='Kredarica' src='../vreme/onlinePictures/SmarnaGora.jpg'  width='105' height='75'></div>";
        
        //info Window Kredarica
        infoWindowKredarica = new google.maps.InfoWindow();
        infoWindowKredarica.setOptions({
           content: contetnKredarica,
           position: {lat: 46.478864, lng: 13.84},
        });
        infoWindowKredarica.open(map);

        //info Window Kamnisko
        infoWindowKamnisko = new google.maps.InfoWindow();
        infoWindowKamnisko.setOptions({
           content: contetnKamnisko,
           position: pKamnisko,
        });
        infoWindowKamnisko.open(map);
        //info Window Smarna gora
        infoWindowSmarna = new google.maps.InfoWindow();
        infoWindowSmarna.setOptions({
           content: contetnSmarna,
           position: pSmarna,
        });
        infoWindowSmarna.open(map);

        // The marker for Kredarica
        var markerTriglav = new google.maps.Marker({position: pKredarica, map: map, label:"Kredarica"});
        markerTriglav.addListener('click', function() {
           infoWindowKredarica.open(map, markerTriglav);
        });
        // The marker for Kamnisko
        var markerKamnisko = new google.maps.Marker({position: pKamnisko, map: map, label:"Kamniško"});
        markerKamnisko.addListener('click', function() {
           infoWindowKamnisko.open(map, markerKamnisko);
        });
        // The marker for Smarna
        var markerSmarna = new google.maps.Marker({position: pSmarna, map: map, label:"Šmarna"});
        markerSmarna.addListener('click', function() {
           infoWindowSmarna.open(map, markerSmarna);
        });
         
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCn1llfsC0Yu29NAnvh9vUPx1CSRuG6HrQ&callback=initMap"
    async defer></script>
  <script type="text/javascript" src="script/pageDefault.js"></script> 
</body>
</html>
