<?php


require 'config.php';
if(!loggedIn()):
    header('Location: main.php');
    endif;

if(admin()):
    header('Location: index.php');
    endif;
    
$collection->deleteOne(['_id' => new MongoDB\BSON\ObjectID($_GET['id'])]);


$_SESSION['success'] = "Data deleted successfully";
header("Location: main.php");


?>
