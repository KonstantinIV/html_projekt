<?php

    $uname = $_POST['postUserID'];
    $passwd = $_POST['postPassID'];

    system('get_graph.exe '.$uname.' '.$passwd.' 2>&1', $retw);
    

    echo "graafik.png";

?>
