<?php

$server = "localhost"; //"magserver";
  $dbusername = "root"; //"subscribe";
  $dbpassword = ""; //"subpass";
  $dbname = "aberloon";

 $conn = mysqli_connect($server,$dbusername, $dbpassword,$dbname);
 $sql = "SELECT PupilID, FirstName, LastName, DateOfBirth, RegClass FROM PupilData;";

$result = mysqli_query($conn,$sql);

echo $sql; // shows the concatenated string
while($row = $result->fetch_assoc()) {
    echo "<p>";
    if($row['RegClass'] == "6A"){
        echo "<b>";
    echo $row['PupilID'] . " - " . $row['FirstName'] . $row['LastName'] . "(" . $row['DateOfBirth'] . ") who is in reg class " . $row['RegClass'];
    echo "</b>";
    } elseif($row['RegClass'] == "6B"){
        echo "<i>";
    echo $row['PupilID'] . " - " . $row['FirstName'] . $row['LastName'] . "(" . $row['DateOfBirth'] . ") who is in reg class " . $row['RegClass'];
    echo "</i>";
    } else {
        echo $row['PupilID'] . " - " . $row['FirstName'] . $row['LastName'] . "(" . $row['DateOfBirth'] . ") who is in reg class " . $row['RegClass'];
    }
    echo "</p>";
}

mysqli_close($conn);

?>