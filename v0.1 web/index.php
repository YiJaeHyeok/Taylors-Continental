<?php

    include_once ('config.php');
?>

<html>
<head>
  <title>Continental System</title>
</head>
<body>
<p>Index PHP<p>
  <?php if(!loggedIn()):?>
    <a href="join.php">Register</a> |
    <a href="login.php">Login</a> 
  <?php else:
    print("Welcome to the members page <b>".$_SESSION["login"]."</b><br>\n");?>
    <a href="logout.php">Logout</a>
    <a href="main.php">Tire Management</a>
  <?php endif;?>
</body>
</html>