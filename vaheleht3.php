<!DOCTYPE html>
<html>
<head>
<title>Leegid peale</title>

</head>

   
<body >
<?php
    echo '<pre>';
    
    // Outputs all the result of shellcommand "ls", and returns
    // the last output line into $last_line. Stores the return value
    // of the shell command in $retval.
    $last_line = shell_exec("webscrape.exe", $retval);
    
    // Printing additional info
    echo '
    </pre>
    <hr />Last line of the output: ' . $last_line . '
    <hr />Return value: ' . $retval;
?>
</body>
</html>
