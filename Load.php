<?php

$conn = new mysqli("localhost", "root", "", "chat_database");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sender = $_GET["sender"] ?? "";
$receiver = $_GET["receiver"] ?? "";

if ($sender && $receiver) {

    $stmt = $conn->prepare("
        SELECT * FROM messages 
        WHERE (sender=? AND receiver=?) 
           OR (sender=? AND receiver=?)
        ORDER BY created_at ASC
    ");

    $stmt->bind_param("ssss", $sender, $receiver, $receiver, $sender);
    $stmt->execute();

    $result = $stmt->get_result();

    while ($row = $result->fetch_assoc()) {
        $class = ($row["sender"] == $sender) ? "user" : "receiver";

        echo "<div class='message $class'>";
        echo "<span>".$row["message"]."</span>";
        echo "</div>";
    }

    $stmt->close();
}

$conn->close();

?>