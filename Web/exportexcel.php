<?php

// Connect to MongoDB
include_once("config.php");
echo "Arrival Form Downloaded!";



// Find all documents in the collection
$documents = $collection->find();

// Open the CSV file for writing
$file = fopen("Arrival Form.csv", "w");

// Write the header row to the CSV file
fputcsv($file, ["DOT", "Date", "Tire_Size","Pattern","Brand"]);

// Write the data to the CSV file
foreach ($documents as $document) {
  fputcsv($file, [$document["DOT"], $document["Date"], $document["Tire_Size"],$document["Pattern"],$document["Brand"]]);
}





?>
<br>
<a href="main.php" class="btn btn-info">Back</a>
