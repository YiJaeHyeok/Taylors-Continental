<?php
include_once("config.php");
if(loggedIn()&&(!(admin()))):
    header('Location: index.php');
endif;


if(isset($_POST["submit"])):
	if(!($_POST["password"] == $_POST["password2"])):
		echo "<p>Your passwords did not match</p>";
		exit;
	endif;
	
    $query = $userdatabase->findOne(array('login' => $_POST['login']));

	if(empty($query)):
		newUser($_POST["login"], $_POST["password"], $_POST["role"], $_POST["details"]);
		cleanMemberSession($_POST["login"], $_POST["password"], $_POST["role"]);
		header("Location: administrator.php");
	else:
	  echo '<p>Username already exists, please choose another username.</p>';
	endif;
endif;
?>

<html>
<head>
  <title>Simple Authentication with MongoDB</title>
</head>
<body>
<form action="<?=$_SERVER["PHP_SELF"];?>" method="POST">
  <table>
  <tr>
    <td>
      Login:
    </td>
    <td>
      <input type="text" name="login" value="<?php print isset($_POST["login"]) ? $_POST["login"] : "" ; ?>"maxlength="15">
    </td>
  </tr>
  <tr>
    <td>
	  Password:
    </td>
	<td>
      <input type="password" name="password" value="" maxlength="15">
    </td>
  </tr>
  <tr>
    <td>
      Confirm password:
    </td>
    <td>
      <input type="password" name="password2" value="" maxlength="15">
    </td>
  </tr>
  <tr>
    <td>
	  Role:
    </td>
	<td>
  <select name="role" id="role">
        	<option value="User">User</option>
        	<option value="Admin">Admin</option>
          </option>
        </select>    </td>
  </tr>
  <tr>
    <td>
	  Details:
    </td>
	<td>
      <input type="details" name="details" value="" maxlength="50">
    </td>
  </tr>
  <tr>
    <td>
      &nbsp;
	</td>
    <td>
      <input name="submit" type="submit" value="Submit">
    </td>
  </tr>
</table>
</form>
</body>
</html>
