<?php
class HandlingDB {
    
    function readPost(){
        $this->user=$_POST['User'];
        $this->password=$_POST['Password'];
    }
    
    function login(){
        
      $servername = "localhost";
      $username = "user";
      $password = "user";
      $dbname = "vaja";
      
      $this->readPost();
      $conn = mysqli_connect($servername, $username, $password, $dbname);
      if (!$conn) {
       die("Connection failed: " . mysqli_connect_error());
      }
      echo "Connected successfully<br>";
      
      $sql = "SELECT user, password FROM customer Where user= 'user'";
      $result = mysqli_query($conn, $sql);
      $row = mysqli_fetch_assoc($result);
      $sqlUser = $row["user"];
      $sqlPassword= $row["password"];
      //wrong data, user or passord is not correct, go back to first page
      if (!(($_SESSION["User"]==$sqlUser) && ($_SESSION["Password"]==$sqlPassword))){
        header("Location: /index.php");  
      }

      //user is admin, if password is corect go to apache root folder    
    }
    
    function adminLogin(){
      $servername = "localhost";
      $username = "user";
      $password = "user";
      $dbname = "vaja";
      
      $this->readPost();
      $conn = mysqli_connect($servername, $username, $password, $dbname);
      if (!$conn) {
       die("Connection failed: " . mysqli_connect_error());
      }
      echo "Connected successfully<br>";
      
      $sql = "SELECT user, password FROM customer Where user= 'admin'";
      $result = mysqli_query($conn, $sql);
      $row = mysqli_fetch_assoc($result);
      $sqlUser = $row["user"];
      $sqlPassword= $row["password"];

      //ce je za admin pravilno geslo in user mu daj vpogled v celotno mapo
      if (($_SESSION["User"]==$sqlUser) && ($_SESSION["Password"]==$sqlPassword)){
        header("Location: /Maketa");  
      }
      //ce se geslo in user ne skladata ga daj nazaj v index
      if (!(($_SESSION["User"]==$sqlUser) && ($_SESSION["Password"]==$sqlPassword))){
        header("Location: /index.php");  
      }
    }
    
    function connectDB($DB){
        
        $servername = "localhost";
        $username = "user";
        $password = "user";
        $dbname = $DB;
    // Create connection
        $conn = mysqli_connect($servername, $username, $password, $dbname);
        // Check connection
        if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
        }
        
        mysqli_query($conn,"SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'");
        return($conn);    
    }
    
    function connectToDB($servername, $username, $password, $dbname){
    // Create connection
        $conn = mysqli_connect($servername, $username, $password, $dbname);
        // Check connection
        if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
        }
        
        mysqli_query($conn,"SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'");
        return($conn);    
    }
    
    function queryTemper($start, $end, $order){
    // Create connection
        $conn = mysqli_connect("localhost", "webScreping", "webScreping", "webScraping");   //$servername, $username, $password, $dbname
        // Check connection
        if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
        }
        //enable UNICODE character
        mysqli_query($conn,"SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'");
        $sql = "SELECT Dan, Kredarica, Ljubljana, Koper FROM temper
                WHERE  Dan >= '$start' AND Dan <= '$end'";
        $sql=$sql . $order . ";"; //sql stavku dodaj order by
            $result = mysqli_query($conn, $sql);
        if (mysqli_num_rows($result) > 0) {
        // output data of each row
            while($row = mysqli_fetch_assoc($result)) {
                $date=$row["Dan"];
                $dateIn=strtotime($date);
                $dateSlo=date("d.m.Y",$dateIn);
                echo "<tr><td>".$dateSlo."</td><td>".$row["Kredarica"]." °C"."</td><td>".$row["Ljubljana"]." °C"."</td><td>".$row["Koper"]." °C"."</td></tr>";
            }
        }
    }
    
    function querySneg($start, $end, $order){
    // Create connection
        $conn = mysqli_connect("localhost", "webScreping", "webScreping", "webScraping");   //$servername, $username, $password, $dbname
        // Check connection
        if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
        }
        //enable UNICODE character
        mysqli_query($conn,"SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'");
        $sql = "SELECT Dan, Kredarica, Zavizan, Ljubljana FROM sneg
                WHERE  Dan >= '$start' AND Dan <= '$end'";
        $sql=$sql . $order . ";"; //sql stavku dodaj order by
            $result = mysqli_query($conn, $sql);
        if (mysqli_num_rows($result) > 0) {
        // output data of each row
            while($row = mysqli_fetch_assoc($result)) {
                $date=$row["Dan"];
                $dateIn=strtotime($date);
                $dateSlo=date("d.m.Y",$dateIn);
                echo "<tr><td>".$dateSlo."</td><td>".$row["Kredarica"]."</td><td>".$row["Zavizan"]."</td><td>".$row["Ljubljana"]."</td></tr>";
            }
        }
    }
    
    function queryWarning($start, $end, $order){
    // Create connection
        $conn = mysqli_connect("localhost", "webScreping", "webScreping", "webScraping");   //$servername, $username, $password, $dbname
        // Check connection
        if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
        }
        //enable UNICODE character
        mysqli_query($conn,"SET character_set_results = 'utf8', character_set_client = 'utf8', character_set_connection = 'utf8', character_set_database = 'utf8', character_set_server = 'utf8'");
        $sql = "SELECT dan, opoz FROM opozorila
                WHERE  Dan >= '$start' AND Dan <= '$end'";
        $sql=$sql . $order . ";"; //sql stavku dodaj order by
            $result = mysqli_query($conn, $sql);
        if (mysqli_num_rows($result) > 0) {
        // output data of each row
            while($row = mysqli_fetch_assoc($result)) {
                $date=$row["dan"];
                $dateIn=strtotime($date);
                $dateSlo=date("d.m.Y",$dateIn);
                echo "<tr><td>".$dateSlo."</td><td>".$row["opoz"]."</td></tr>";
            }
        }
    }


}
?>


