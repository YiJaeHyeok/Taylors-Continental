<?php

require_once ('config.php');
if(!loggedIn()):
   header('Location: index.php');

elseif(!admin()):
   header('Location: index.php');
   
else:
if (isset($_GET['id'])) {
   $tires = $userdatabase->findOne(['_id' => new MongoDB\BSON\ObjectID($_GET['id'])]);
}


if(isset($_POST['submit'])){


   $userdatabase->updateOne(
       ['_id' => new MongoDB\BSON\ObjectID($_GET['id'])],
       ['$set' => ['DOT' => $_POST['DOT'], 'Date' => $_POST['Date'],
       'Tire_Size' => $_POST['Tire_Size'],'Pattern' => $_POST['Pattern'],'Brand' => $_POST['Brand']]]
   );


   $_SESSION['success'] = "Data updated successfully";
   header("Location: main.php");
}


?>


<!DOCTYPE html>
<html>
<head>
   <title>Edit Data</title>
   <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
</head>
<body>


<div class="container">
   <h1>Edit Data</h1>
   <a href="index.php" class="btn btn-primary">Back</a>


   <form method="POST">
      <div class="form-group">
         <strong>DOT:</strong>
         <input type="text" name="DOT" value="<?php echo $tires->DOT; ?>" required="" class="form-control" placeholder="DOT">
      </div>
      <div class="form-group">
         <strong>Date:</strong>
         <textarea class="form-control" name="Date" placeholder="Date" placeholder="Date"><?php echo $tires->Date; ?></textarea>
      </div>
      <div class="form-group">
         <strong>Tire Size:</strong>
         <textarea class="form-control" name="Tire_Size" placeholder="Tire_Size" placeholder="Tire_Size"><?php echo $tires->Tire_Size; ?></textarea>
      </div>
      <div class="form-group">
         <strong>Pattern:</strong>
         <textarea class="form-control" name="Pattern" placeholder="Pattern" placeholder="Pattern"><?php echo $tires->Pattern; ?></textarea>
      </div>
      <div class="form-group">
         <strong>Brand:</strong>
         <textarea class="form-control" name="Brand" placeholder="Brand" placeholder="Brand"><?php echo $tires->Brand; ?></textarea>
      </div>
      <div class="form-group">
         <button type="submit" name="submit" class="btn btn-success">Submit</button>
      </div>
   </form>
</div>


</body>
</html>
<?php endif; ?>