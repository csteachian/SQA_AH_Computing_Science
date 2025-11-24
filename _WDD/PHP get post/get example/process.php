<?php
// Check that data exists before using it
if (isset($_GET['name']) && isset($_GET['age'])) {

    $name = $_GET['name'];
    $age = $_GET['age'];

    echo "<h2>Form Results</h2>";
    echo "Your name is: " . htmlspecialchars($name) . "<br>";
    echo "Your age is: " . htmlspecialchars($age);

} else {
    echo "No form data received.";
}
?>
