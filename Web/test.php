<?php
require_once ('config.php');

$regex = new MongoDB\BSON\Regex ( '2');
$cursor = $collection->find(array('Brand' => $regex));
//iterate through the cursor

foreach ($cursor as $doc) {
    var_dump($doc);
}