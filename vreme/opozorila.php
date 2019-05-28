<?php
    session_start();    
    //Sortiraj-preberi iz sessiona spremenljivke
    if ( empty($_POST)) {
        $now = time();
        $hist=strtotime("-2 month",$now);
        $nowSlo=date("d.m.Y", $now);
        $nowUSA=date("Y-m-d",$now);
        $histSlo=date("d.m.Y", $hist);
        $histUSA=date("Y-m-d",$hist);
    }
    if(!empty($_SESSION)){
        $histUSA = $_SESSION['startDate'];
        $nowUSA=$_SESSION['endDate'];
        $hist=strtotime($histUSA);
        $now=strtotime($nowUSA);
        $histSlo=date("d.m.Y", $hist);
        $nowSlo=date("d.m.Y", $now);
    }
    if (!empty($_POST)){
        $histSlo=$_POST['startDate'];
        $nowSlo=$_POST['endDate'];
        $hist=strtotime($histSlo);
        $now=strtotime($nowSlo);
        $histUSA=date("Y-m-d", $hist);
        $nowUSA=date("Y-m-d",$now);
    }
?>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="../vreme/Desigen/main2.css"><!--barve oblikae okna-->
        <link rel="stylesheet" type="text/css" href="../vreme/Desigen/table.css3"> <!--lastnosti in animacija glavne tabele-->
	<!--for a bootstrap-->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
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



    <div class="container">

        <h2>Prikaži zgodovino izdanih opozoril ARSO</h2>
        <form method="post" action="sneg.php" >
          <div class="form-group">
            <label for="startDate">Od datuma:</label>
            <input class="form-control" type="text" name="startDate" value="<?php echo $histSlo?>"
          </div>
          <div class="form-group">
            <label for="startDate">Od datuma:</label>
            <input class="form-control" type="text" name="endDate" value="<?php echo $nowSlo?>"
          </div>
         <input type="submit" class="btn btn-default" VALUE = "Potrdi">
         </form>

    <!-- glava tabele -->
        <table id=t01 border='1' style='width:80%'>
        <tr><th><a href="/vreme/opozorila.php?sort=Dan">Dan</a></th><th> Opozorila </th></tr>
        </div>
        


        <script type="text/javascript" src="script/pageDefault_2.js"></script> 
        <script>
            function home(){
                window.location='../vreme/index.php';
            }
            //function sortInput(x1,x2){
            //    document.getElementById("i1").value=x1;
            //    document.getElementById("i2").value=x2;
            //}
        </script>
    </body>
</html>
<?php
// naredi objekt iz razreda, ki je v datoteki /vreme/handlingDB.inc
    require_once ('../vreme/handlingDB.inc');
    $queryDB= new HandlingDB;
    $_SESSION['count']++; //steve s pomocjo katerga bos razvrsal od vecjega k manjsemu

// izberi razvrstitev
    if(($_SESSION['count']%2==0) && ($_GET['sort']=="Dan")){
        $order=" ORDER BY Dan DESC";
        $queryDB->queryWarning($histUSA, $nowUSA, $order);
    }
    elseif(($_SESSION['count']%2==1) && ($_GET['sort']=="Dan")){
        $order=" ORDER BY Dan ASC";
        $queryDB->queryWarning($histUSA, $nowUSA, $order);
    }

    else{
        $order=" ORDER BY Dan DESC";
        $queryDB->queryWarning($histUSA, $nowUSA, $order);
    }

    
// v sesion vpisi ali podatke iz $xyUSA (doloceno na zacetku programa)
// ali pa iz vnosnega polja, ki preko $_POST doloci nov datum 
    if(empty($_POST)){    
        $_SESSION['startDate'] = $histUSA;
        $_SESSION['endDate'] = $nowUSA;
        $hist=strtotime($histUSA);
        $now=strtotime($nowUSA);
        $histSlo=date("d.m.Y",$hist);
        $nowSlo=date("d.m.Y",$now);
    }else{
        $hist=strtotime($histSlo);
        $now=strtotime($nowSlo);
        $_SESSION['startDate'] = date("Y-m-d",$hist);
        $_SESSION['endDate'] = date("Y-m-d",$now);       
    }
//print_r($_POST);  
?>
