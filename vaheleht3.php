<!DOCTYPE html>
<html>
<head>
<title>Leegid peale</title>
<link rel="stylesheet" type="text/css" href="CSS_kaust/style.css">
</head>

   
<body style="background-color:white;">

<div id="container">       
    <form action="vaheleht3.php" method="post">
        <label for="username">Username:</label>
            <input type="text" id="username" name="username">
        <br>
        <label for="password">Password:</label>
            <input type="password" id="password" name="password">
        <br>
        <div id="lower">
            <input type="submit"  name="someAction">
        </div><!--/ lower-->
    </form>
</div>

<?php
     if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['someAction']))
     {
         func($_POST['username'],$_POST['password']);
     }
     function func($a,$b)
     {
        $last_line = exec('python test.py '.$a.' '.$b, $retval);
        
        //echo 'Last line of the output: ' . $last_line;    
        echo '<img src="world.svg">';
        //$last_line2 = exec('cat maier.txt', $retval2);
        //echo ' output: '. $last_line2;  
     }
   
    
?>
</body>
</html>
