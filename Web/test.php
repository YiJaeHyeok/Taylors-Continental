<?php
require 'vendor/autoload.php';
// Creating Connection
$con = new MongoDB\Client("mongodb://localhost:27017");
// Creating Database
$db = $con->javatpoint;
// Creating Document
$collection = $db->employee;
// Insering Record
$collection->insertOne( [ 'name' =>'Peter', 'email' =>'peter@abc.com' ] );
// Fetching Record
$record = $collection->find( [ 'name' =>'Peter'] );
foreach ($record as $employe) {
echo 'Name :'$employe['name'], ': ', $employe['email']."<br>";
}
?>
