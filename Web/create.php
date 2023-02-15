<?php


require_once ('config.php');
if(!loggedIn()):
   header('Location: main.php');
   
elseif(admin()):
   header('Location: index.php');
   
else:

if(isset($_SESSION['error'])){
   echo "<div class='alert alert-danger'>".$_SESSION['error']."</div>";
}
if(isset($_POST['submit'])){
   // Check if input contains special characters
   if(preg_match('/[^A-Za-z0-9_]/', $_POST['DOT']) ||
      preg_match('/[^A-Za-z0-9_]/', $_POST['Date']) ||
      preg_match('/[^A-Za-z0-9_]/', $_POST['Tire_Size']) ||
      preg_match('/[^A-Za-z0-9_]/', $_POST['Pattern']) ||
      preg_match('/[^A-Za-z0-9_]/', $_POST['Brand'])){

      $_SESSION['error'] = "Input cannot contain special characters";
      header("Location: create.php");
exit;
   }

   $insertOneResult = $collection->insertOne([
       'DOT' => $_POST['DOT'],
      'Date' => $_POST['Date'],
       'Tire_Size' => $_POST['Tire_Size'],
       'Pattern' => $_POST['Pattern'],
      'Brand' => $_POST['Brand'],
  ]);
  $_SESSION['success'] = "Data added successfully";
  header("Location: main.php");
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
   <a href="main.php" class="btn btn-primary">Back</a>


   <form method="POST">
      <div class="form-group">
         <strong>DOT:</strong>
         <input type="text" name="DOT" required="" class="form-control" placeholder="DOT">
      </div>
      <div class="form-group">
         <strong>Date:</strong>
         <textarea class="form-control" name="Date" placeholder="Date" placeholder="Date"></textarea>
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
<?php endif; ?>