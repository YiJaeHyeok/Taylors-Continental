<?php
require_once ('config.php');

$filter  = [];
$options = ['sort' => ['password' => 1]];

$cursor=$userdatabase->find($filter, $options);

foreach($cursor as $result)
{
    print_r($result);
}
?>