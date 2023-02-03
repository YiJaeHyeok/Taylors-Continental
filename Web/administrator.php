<?php
include_once("config.php");


require_once ('config.php');
if(!loggedIn()):
   header('Location: index.php');
   endif;

if(!admin()):
   header('Location: index.php');
   endif;


?>
<!DOCTYPE html>
<html>

<head>
   <title>User Administration</title>
   <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous" >

</head>
<body>


<div class="container">
<h1>User Administration</h1>


<?php

   if(isset($_SESSION['success'])){
      echo "<div class='alert alert-success'>".$_SESSION['success']."</div>";
   }

?>


<table class="table table-borderd">
   <tr>
      <th>Login ID</th> 
      <th>Role</th>
      <th>Details</th>

   </tr>
   <?php

      $users = $userdatabase->find();

      foreach($users as $users) {
         echo "<tr>";
         echo "<td>".$users->login."</td>";
         echo "<td>".$users->role."</td>";
         echo "<td>".$users->details."</td>";
         #echo "<td>".$users->role."</td>";
         #echo "<td>".$users->details."</td>";

         echo "<td>";
         echo "<a href='edit.php?id=".$users->_id."' class='btn btn-primary'>Edit</a>";
         echo "<a href='deleteUser.php?id=".$users->_id."' class='btn btn-danger'>Delete</a>";
         echo "</td>";
         echo "</tr>";
      };


   ?>
</table>
<a href="main.php" class="btn btn-success">Back</a>
<a href="administrator.php" class="btn btn-success">Export to Excel</a>
<a href="join.php" class="btn btn-success">Add User</a>
</div>
</body>
</html>
