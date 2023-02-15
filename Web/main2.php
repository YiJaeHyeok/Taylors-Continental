<?php
include_once("config.php");

if(!loggedIn()):
header('Location: index.php');
endif;

if(admin()):
   header('Location: index.php');
   endif;

//sorting
   $cursor = $collection->find();
   $tires = iterator_to_array($cursor);

   if (isset($_POST['DOTSORT2'])) {
     if ($_POST['DOTSORT'] == 'ASC') {
       usort($tires, function($a, $b) {
         return $a['DOT'] <=> $b['DOT'];
       });
     } else {
       usort($tires, function($a, $b) {
         return $b['DOT'] <=> $a['DOT'];
       });
     }
   }

   if (isset($_POST['DateSORT2'])) {
     if ($_POST['DateSORT'] == 'ASC') {
       usort($tires, function($a, $b) {
         return $a['Date'] <=> $b['Date'];
       });
     } else {
       usort($tires, function($a, $b) {
         return $b['Date'] <=> $a['Date'];
       });
     }
   }

   if (isset($_POST['size2'])) {
     if ($_POST['size'] == 'ASC') {
       usort($tires, function($a, $b) {
         return $a['Tire_Size'] <=> $b['Tire_Size'];
       });
     } else {
       usort($tires, function($a, $b) {
         return $b['Tire_Size'] <=> $a['Tire_Size'];
       });
     }
   }
   if (isset($_POST['pattern2'])) {
     if ($_POST['pattern'] == 'ASC') {
       usort($tires, function($a, $b) {
         return $a['Pattern'] <=> $b['Pattern'];
       });
     } else {
       usort($tires, function($a, $b) {
         return $b['Pattern'] <=> $a['Pattern'];
       });
     }
   }
   if (isset($_POST['brand2'])) {
     if ($_POST['brand'] == 'ASC') {
       usort($tires, function($a, $b) {
         return $a['Brand'] <=> $b['Brand'];
       });
     } else {
       usort($tires, function($a, $b) {
         return $b['Brand'] <=> $a['Brand'];
       });
     }
   }

   if (isset($_POST['search'])) {
   $search_query = $_POST['search_query'];
   // Search for documents that match the search query
   $search_results = $collection->find([
   '$or' => [
   ['Tire_Size' => ['$regex' => $search_query]],
   ['Brand' => ['$regex' => $search_query]],
   ['Pattern' => ['$regex' => $search_query]],
   ['Date' => ['$regex' => $search_query]],
   ['DOT' => ['$regex' => $search_query]]
   ]
   ]);
   } else {
     // If the search form is not submitted, show all documents
     $search_results = $collection->find();
   }

?>
<!DOCTYPE html>
<html>

<head>
   <title>Database Management</title>
   <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous" >

</head>
<body>


<div class="container">
<h`1`>Data Management</h1>
<br>


<form action="" method="post">
  <input type="text" name="search_query">
  <input type="submit" name="search" value="Search" class="btn btn-success">
</form>



<?php
   if(isset($_SESSION['success'])){
      echo "<div class='alert alert-success'>".$_SESSION['success']."</div>";
   }
?>

<table class="table table-borderd">
   <tr>
      <th>DOT
        <form method="post">
            <select name="DOTSORT">
                <option value="">Choose</option>
                <option value="ASC">Ascending</option>
                <option value="DESC">Descending</option>
            </select>
            <input type="submit" name="DOTSORT2" value="Sort">
        </form>
      </th>
      <th>Date
        <form method="post">
            <select name="DateSORT">
                <option value="">Choose</option>
                <option value="ASC">Ascending</option>
                <option value="DESC">Descending</option>
            </select>
            <input type="submit" name="DateSORT2" value="Sort">
        </form>
      </th>
      <th>Tire Size
        <form method="post">
            <select name="size">
                <option value="">Choose</option>
                <option value="ASC">Ascending</option>
                <option value="DESC">Descending</option>
            </select>
            <input type="submit" name="size2" value="Sort">
        </form>
      </th>
      <th>Pattern
        <form method="post">
            <select name="pattern">
                <option value="">Choose</option>
                <option value="ASC">A ~ Z</option>
                <option value="DESC">Z ~ A</option>
            </select>
            <input type="submit" name="pattern2" value="Sort">
        </form>
      </th>
      <th>Brand
        <form method="post">
            <select name="brand">
                <option value="">Choose</option>
                <option value="ASC">A ~ Z</option>
                <option value="DESC">Z ~ A</option>
            </select>
            <input type="submit" name="brand2" value="Sort">
        </form>
      </th>
      <th>Action
        <br>
        <a href="create.php" class="btn btn-warning">Add Data</a>
      </th>
   </tr>
   <?php



      foreach ($search_results as $result) {
        echo "<tr>";
        echo "<td>".$result->DOT."</td>";
        echo "<td>".$result->Date."</td>";
        echo "<td>".$result->Tire_Size."</td>";
        echo "<td>".$result->Pattern."</td>";
        echo "<td>".$result->Brand."</td>";

        echo "<td>";
        echo "<a href='edit.php?id=".$result->_id."' class='btn btn-primary'>Edit</a>";
        echo "<a href='delete.php?id=".$result->_id."' class='btn btn-danger'>Delete</a>";
        echo "</td>";
        echo "</tr>";
      };

   ?>

</table>
<a href="main.php" class="btn btn-info">Back</a>
<a href="exportexcel.php" class="btn btn-success">Export to Excel</a>
<a href="runprogram.php" class="btn btn-success">Start Program</a>
</div>


</body>
</html>
