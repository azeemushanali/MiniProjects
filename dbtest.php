<?php
$servername = "db-assignment-solo-1.cdxhhswkgl8b.us-east-2.rds.amazonaws.com";
$username = "admin";
$password = "root12345";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
