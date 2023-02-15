<?php


require 'config.php';
if(!loggedIn()):
    header('Location: main.php');


elseif(admin()):
    header('Location: index.php');

else:
    
$collection->deleteOne(['_id' => new MongoDB\BSON\ObjectID($_GET['id'])]);


$_SESSION['success'] = "Data deleted successfully";
header("Location: main.php");


?>
<?php endif; ?>