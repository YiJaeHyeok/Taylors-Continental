<?php
require_once ('config.php');

$cursor=$collection->find();
foreach($cursor as $result)
{
    print_r($result);
}
?>
