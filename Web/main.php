<?php
include_once("config.php");

if(!loggedIn()):
header('Location: index.php');

else:
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
<h1>Data Management</h1>
<br>

<form action="main2.php" method="post">
  <input type="text"  name="search_query">
  <input type="submit" name="search" value="Search"class="btn btn-success">
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


   $limit = 20;
 $current_page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
 $start = ($current_page - 1) * $limit;
 $tires_subset = array_slice($tires, $start, $limit);
 $ellipsisAdded = false;
 foreach ($tires_subset as $tire) {
   echo "<tr>";
   echo "<td>".$tire->DOT."</td>";
   echo "<td>".$tire->Date."</td>";
   echo "<td>".$tire->Tire_Size."</td>";
   echo "<td>".$tire->Pattern."</td>";
   echo "<td>".$tire->Brand."</td>";

   echo "<td>";
   echo "<a href='edit.php?id=".$tire->_id."' class='btn btn-primary'>Edit</a>";
   echo "<a href='delete.php?id=".$tire->_id."' class='btn btn-danger'>Delete</a>";
   echo "</td>";
   echo "</tr>";
 };

 $total_pages = ceil(count($tires) / $limit);
 echo "<nav aria-label='Page navigation example'>";
 echo "<ul class='pagination justify-content-center'>";

 if ($current_page > 1) {
   echo "<li class='page-item'>";
   echo "<a class='page-link' href='?page=".($current_page - 1)."' tabindex='-1'>Previous</a>";
   echo "</li>";
 }
 
 for ($i = 1; $i <= $total_pages; $i++) {
  if ($total_pages > 10 && abs($i - $current_page) > 2 && $i != 1 && $i != $total_pages) {
    if ($i > $current_page && $ellipsisAdded != 'right') {
      echo "<li class='page-item disabled'><span class='page-link'>...</span></li>";
      $ellipsisAdded = 'right';
    } elseif ($i < $current_page && $ellipsisAdded != 'left') {
      echo "<li class='page-item disabled'><span class='page-link'>...</span></li>";
      $ellipsisAdded = 'left';
    }
    continue;
  }
  echo "<li class='page-item ".($i === $current_page ? 'active' : '')."'>";
  echo "<a class='page-link' href='?page=".$i."'>".$i."</a>";
}

 if ($current_page < $total_pages) {
   echo "<li class='page-item'>";
   echo "<a class='page-link' href='?page=".($current_page + 1)."'>Next</a>";
   echo "</li>";
 }

 echo "</ul>";
 echo "</nav>";



   ?>

</table>
<a href="index.php" class="btn btn-info">Back</a>
<a href="exportexcel.php" class="btn btn-success">Export to Excel</a>

</div>


</body>
</html>
<?php endif; ?>