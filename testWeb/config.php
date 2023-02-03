<?php
ob_start();
error_reporting(E_ALL);
try{
    require_once __DIR__ .'/vendor/autoload.php';
    $con = new MongoDB\Client("mongodb://root:root@localhost:27017");
    $db   = $con->User;
    $coll = $db->users;
}

    catch (MongoConnectionException $e){
        die('Error connecting to MongoDB server');
} 

    catch (MongoException $e) {
        die('Error: ' . $e->getMessage());
}

session_start();
	if(!(isset($_SESSION['loggedIn']))):
		{
			$_SESSION['login']='';
			$_SESSION['password']='';
			$_SESSION['loggedIn']='';	
		}
	endif;


function newUser($login, $password)
{
	global $coll;
	$coll->insertOne(array('login' => $login, 'password' => md5($password)));
	return true;
}

function checkPass($login, $password) 
{
	global $coll;
	$res = $coll->findOne(array('login' => $login, 'password' => md5($password)));
	if($res):
	return true;
	endif;
}

function cleanMemberSession($login, $password)
{

	$_SESSION["login"]=$login;
	$_SESSION["password"]=$password;
	$_SESSION["loggedIn"]=true;
}

function flushMemberSession()
{
	unset($_SESSION["login"]);
	unset($_SESSION["password"]);
	unset($_SESSION["loggedIn"]);
	session_destroy();
	return true;
}

function loggedIn()
{
	if($_SESSION['loggedIn']):
	  return true;
	else:
	  return false;
	endif;
}
  
?>