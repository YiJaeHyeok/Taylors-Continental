<?php


require 'config.php';
if(!loggedIn()):
    header('Location: administration.php');
    endif;

$userdatabase->deleteOne(['_id' => new MongoDB\BSON\ObjectID($_GET['id'])]);

$_SESSION['success'] = "Data deleted successfully";
header("Location: administrator.php");


?>
