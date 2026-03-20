<?php

$conn = new mysqli("localhost", "root", "");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "CREATE DATABASE chat_database";

if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
} else {
    echo "Error: " . $conn->error;
}

$conn->close();

?>