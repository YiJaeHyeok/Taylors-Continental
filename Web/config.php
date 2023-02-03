<?php
ob_start();
error_reporting(E_ALL);
try{
    require_once __DIR__ .'/vendor/autoload.php';
    $con = new MongoDB\Client("mongodb://root:root@localhost:27017");
    $db   = $con->User;
    $userdatabase = $db->users;
	$collection = (new MongoDB\Client)->Continental->tires;

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


function newUser($login, $password, $role ,$details)
{
	global $userdatabase;
	$userdatabase->insertOne(array('login' => $login, 'password' => md5($password), 'role' => $role, 'details' => $details));
	return true;
}

function checkPass($login, $password) 
{
	global $userdatabase;
	$res = $userdatabase->findOne(array('login' => $login, 'password' => md5($password)));
	#	findOne(array('login' => 'admin', 'password' => md5($password)));
	if($res):		
	$_SESSION['role']=$res->role;
	return true;
	endif;
}

function cleanMemberSession($login, $password)
{

	$_SESSION["login"]=$login;
	$_SESSION["password"]=$password;
	#$_SESSION["role"]=$role;
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
  
function admin()
{
	if($_SESSION['role']=='Admin'):
	  return true;
	else:
	  return false;
	endif;
}

?>