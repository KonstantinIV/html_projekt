<!DOCTYPE html>
<html>
<head>
<title>Leegid peale</title>

<link rel="stylesheet" type="text/css" href="CSS_kaust/style.css">
<link rel="stylesheet" type="text/css" href="CSS_kaust/login.css" />

</head>

   
<body style="background-color:none;">
<body >
        <header>
                <div class="header_logo_container">
                    <div class=" header_cont">
                        <h1 class="main_header">ABSOLUTELY LIT INC.</h1>
                        <p class="content_box_text_header">Parim tööriist Moodle'i kursuste hinnete jälgimiseks
                        , mis annab suurepärase ülevaate olukorrast. Hoiab teid kursis ning aitab teil planeerida
                        oma õpinguid mitu korda paremini.
                            </p>
                    </div> 
                    <div id="fire_container"><img id="fire_logo" src="Piltmaterjal/logo.svg" ></div>
                </div>
            
                <div class="navi">
                    <ul>
                        <li ><a href="vaheleht1.html">Vaheleht</a></li>
                        <li ><a  href="pealeht.html">Pealeht</a></li>
                        <li ><a class="active" href="vaheleht2.php">Vaheleht</a></li>
                    </ul> 
                    
                </div>
            </header>

<div style="position:relative;">
<form action="vaheleht3.php" method="post">
        <div class="imgcontainer">
            <img src="Piltmaterjal/stockvault-anonymous-businessman-with-derby-hat180437.jpg" alt="Avatar" class="avatar">
        </div>
        
        <div class="container">
            <label for="uname"></label>
            <input type="text" placeholder="Enter Username" name="username" required>
        
            <label for="psw"></label>
            <input type="password" placeholder="Enter Password" name="password" required>
                
            <button type="submit"  name="someAction">Login</button>
        </div>
    </form>
</div>
<?php
     if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['someAction']))
     {
         func($_POST['username'],$_POST['password']);
     }
     function func($a,$b)
     {
        #$last_line = exec('python test.py '.$a.' '.$b, $retval);
        $last_line = exec("python matplot.py", $retval);
        //echo 'Last line of the output: ' . $last_line;    
        echo '<img src="graafik.png">';
        //$last_line2 = exec('cat maier.txt', $retval2);
        //echo ' output: '. $last_line2;  
     }
   
    
?>
<!--FOOTER-------------------------------------------------------------------------------------------------->

<footer>
    <div id="footer_content_container">
        <div id="footer_right_container">
                <p id="footer_header">HELP</p>
                <p id="footer_text">Police</p>
                <p id="footer_text">Ambulance</p>
                <p id="footer_text">Firefighters</p>
        </div>
        <div id="footer_left_container" >
                <p id="footer_header">CONCTACT</p>
                <p id="footer_text">GitHub</p>
                <p id="footer_text">Facebook</p>
                <p id="footer_text">Crapbook</p>

        </div>
    </div>

    <!--Picture-->
    <img id="footer_fire_logo" src="Piltmaterjal/drawing2.svg" >

    <!--Footer line and copyright text-->
        <div  id="copyright_footer_line_container">
            <hr id="footer_line"><div id="copyright_container" >
            <p id="copyright_text" >&copy; 2015 insert very cool website name here.com</p>
        </div>
    </div>
</footer>
</body>
</html>
