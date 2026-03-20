<?php

$conn = new mysqli("localhost", "root", "", "chat_database");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sender = $_POST["sender"] ?? "";
$receiver = $_POST["receiver"] ?? "";
$message = $_POST["message"] ?? "";

if ($sender && $receiver && $message) {

    $stmt = $conn->prepare("INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $sender, $receiver, $message);
    $stmt->execute();
    $stmt->close();
}

$conn->close();

?>