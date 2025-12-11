<?php
  $username = $_POST['username'];
  $password = $_POST['password'];

  $server = "localhost"; //"magserver";
  $dbusername = "root"; //"subscribe";
  $dbpassword = ""; //"subpass";
  $dbname = "subscribedata";

 $conn = mysqli_connect($server,$dbusername, $dbpassword,$dbname);
 $sql = "INSERT INTO member VALUES ('" .
        $username . "', '" . $password . "')";
echo $sql;
mysqli_query($conn,$sql);
mysqli_close($conn);
              

?>