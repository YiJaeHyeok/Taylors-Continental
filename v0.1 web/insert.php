<?php
require_once __DIR__ .'/vendor/autoload.php';
$con = new MongoDB\Client("mongodb://localhost:27017");
//print_r($con);

$db = $con->capstone1;
$tbl = $db ->table1;
$tbl -> insertOne(["Name" => "hello"])



?>
