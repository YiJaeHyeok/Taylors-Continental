<?php


require 'config.php';
if(!loggedIn()):
    header('Location: index.php');
    endif;

$collection->deleteOne(['_id' => new MongoDB\BSON\ObjectID($_GET['id'])]);


$_SESSION['success'] = "Data deleted successfully";
header("Location: index.php");


?>
