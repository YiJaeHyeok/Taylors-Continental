<?php
require_once ('config.php');
if(!loggedIn()):
   header('Location: index.php');

elseif(!admin()):
   header('Location: index.php');
   
else:

$userdatabase->deleteOne(['_id' => new MongoDB\BSON\ObjectID($_GET['id'])]);

$_SESSION['success'] = "Data deleted successfully";
header("Location: administrator.php");

endif;
?>
