<?php

unset($_SESSION);
session_start();

$_SESSION['TEST']='';


if($_SESSION['TEST']):
    echo 'true output';
  else:
    echo 'false output';
  endif;

?>

