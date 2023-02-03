<?php
include_once("config.php");

if(!loggedIn()):
header('Location: index.php');
endif;

?>
<!DOCTYPE html>
<html>

<head>
   <title>Database Management</title>
   <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous" >

</head>
<body>


<div class="container">
<h1>Data Management</h1>


<a href="create.php" class="btn btn-success">Add Data</a>
<a href="create.php" class="btn btn-success">Filter Data</a>




<?php


   if(isset($_SESSION['success'])){
      echo "<div class='alert alert-success'>".$_SESSION['success']."</div>";
   }


?>


<table class="table table-borderd">
   <tr>
      <th>DOT</th>
      <th>TICS</th>
      <th>Tire Size</th>
      <th>Pattern</th>
      <th>Brand</th>
      <th>Action</th>
   </tr>
   <?php



      $tires = $collection->find();


      foreach($tires as $tires) {
         echo "<tr>";
         echo "<td>".$tires->DOT."</td>";
         echo "<td>".$tires->TICS."</td>";
         echo "<td>".$tires->Tire_Size."</td>";
         echo "<td>".$tires->Pattern."</td>";
         echo "<td>".$tires->Brand."</td>";

         echo "<td>";
         echo "<a href='edit.php?id=".$tires->_id."' class='btn btn-primary'>Edit</a>";
         echo "<a href='delete.php?id=".$tires->_id."' class='btn btn-danger'>Delete</a>";
         echo "</td>";
         echo "</tr>";
      };


   ?>
</table>
<a href="create.php" class="btn btn-success">Back</a>
<a href="create.php" class="btn btn-success">Export to Excel</a>
<a href="untitled2.py" class="btn btn-success">Run python Code</a>
</div>
<?php

$pythonoutput = shell_exec("untitled2.py");

echo $pythonoutput;

?>

</body>
</html>
