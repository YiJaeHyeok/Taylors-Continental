<?php
include_once("config.php");

if (($_SERVER["REMOTE_ADDR"]=='127.0.0.1')&&loggedIn()): 
    exec('START C:\Users\contienntal\output\automation_Program\automation_Program.exe');

else: 
    header('Location: index.php');

endif;?>
