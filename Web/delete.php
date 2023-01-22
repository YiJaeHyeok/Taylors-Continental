<?php


session_start();
require 'config.php';


$collection->deleteOne(['_id' => new MongoDB\BSON\ObjectID($_GET['id'])]);


$_SESSION['success'] = "Data deleted successfully";
header("Location: index.php");


?>
