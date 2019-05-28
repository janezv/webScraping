
<!--how can javaScript get array of variable from php-->
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
        <script>
        $(document).ready(function(){
            $("#next").click(function(){
                var someimage = document.getElementById('2');
                var imgSrc= someimage.src;
                $.ajax({
                    url: 'answerAdd.php',
                    type: 'post',
                    data: { "p1": imgSrc},
                    success: function(response) {
                        var odg=response;
                        if (odg) {
                            // alert (odg);
                            document.getElementById('2').src=odg;
                        }
                    }
                });
            });
            $("#previous").click(function(){
                var someimage = document.getElementById('2');
                var imgSrc= someimage.src;
                $.ajax({
                    url: 'answerSubtract.php',
                    type: 'post',
                    data: { "p1": imgSrc},
                    success: function(response) {
                        var odg=response;
                        if (odg) {
                            // alert (odg);
                            document.getElementById('2').src=odg;
                        }
                    }
                });
            });

        });
</script>

    </head>
    <body>
        <img id=previous title="Predhodna slika" src="../vreme/Desigen/previous.jpg" width=65 height=65 style="cursor:pointer">&nbsp  &nbsp &nbsp &nbsp  &nbsp 
        <img id=next title="Naslednja slika" src="../vreme/Desigen/next.jpg" width=65 height=65 style="cursor:pointer">
    </body>
</html>
<?php
    session_start();
    $imgSrc=$_GET['img'];
    echo "<img id=2 src='$imgSrc' height='600' width='800'>";
?>
