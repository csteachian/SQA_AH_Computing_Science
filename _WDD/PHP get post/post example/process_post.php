<?php
// Check if form values exist before using them
if (isset($_POST['name']) && isset($_POST['age'])) {
    $name = $_POST['name'];
    $age = $_POST['age'];

    echo "<h1>Hello, $name!</h1>";
    echo "<p>You are $age years old.</p>";
} else {
    echo "No form data received.";
}
?>

