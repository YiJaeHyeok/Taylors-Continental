<?php


session_start();


if(isset($_POST['submit'])){


   require 'config.php';


   $insertOneResult = $collection->insertOne([
       'DOT' => $_POST['DOT'],
       'TICS' => $_POST['TICS'],
       'Tire_Size' => $_POST['Tire_Size'],
       'Pattern' => $_POST['Pattern'],
       'Brand' => $_POST['Brand'],
   ]);


   $_SESSION['success'] = "Data added successfully";
   header("Location: index.php");
}


?>


<!DOCTYPE html>
<html>
<head>
   <title>Add Data</title>
   <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
</head>
<body>


<div class="container">
   <h1>Add Data</h1>
   <a href="index.php" class="btn btn-primary">Back</a>


   <form method="POST">
      <div class="form-group">
         <strong>DOT:</strong>
         <input type="text" name="DOT" required="" class="form-control" placeholder="DOT">
      </div>
      <div class="form-group">
         <strong>TICS:</strong>
         <textarea class="form-control" name="TICS" placeholder="TICS" placeholder="TICS"></textarea>
      </div>
      <div class="form-group">
         <strong>Tire Size:</strong>
         <textarea class="form-control" name="Tire_Size" placeholder="Tire_Size" placeholder="Tire_Size"></textarea>
      </div>
      <div class="form-group">
         <strong>Pattern:</strong>
         <textarea class="form-control" name="Pattern" placeholder="Pattern" placeholder="Pattern"></textarea>
      </div>
      <div class="form-group">
         <strong>Brand:</strong>
         <textarea class="form-control" name="Brand" placeholder="Brand" placeholder="Brand"></textarea>
      </div>
      <div class="form-group">
         <button type="submit" name="submit" class="btn btn-success">Submit</button>
      </div>
   </form>
</div>


</body>
</html>
