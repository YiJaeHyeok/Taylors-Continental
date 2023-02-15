<?php

    include_once ('config.php');
?>

<html>
<head>
  <title>Continental System</title>
</head>
<body>
<p>Index PHP<p>
  <?php if(!@loggedIn()):?>
    <a href="login.php">Login</a> 
  
  <?php elseif(@loggedIn()&&admin()):
    print("Welcome to the members page <b>".$_SESSION["login"]."</b><br>\n");?>
    <a href="logout.php">Logout</a>
    <a href="main.php">Tire Management</a>
    <a href="administrator.php">User Management</a>
    <?php if ($_SERVER["REMOTE_ADDR"]=='127.0.0.1'): ?>
      <a href="runprogram.php" class="btn btn-success">Start Program</a>
      <a href="stopprogram.php" class="btn btn-success">Stop Program</a>      <?php endif;?>
      
  <?php else:
      print("Welcome to the members page <b>".$_SESSION["login"]."</b><br>\n");?>
    <a href="logout.php">Logout</a>
    <a href="main.php">Tire Management</a>
     <?php if ($_SERVER["REMOTE_ADDR"]=='127.0.0.1'): ?>
      <a href="runprogram.php" class="btn btn-success">Start Program</a>
      <a href="stopprogram.php" class="btn btn-success">Stop Program</a>      <?php endif;?>
  <?php endif;?>
</body>
</html>