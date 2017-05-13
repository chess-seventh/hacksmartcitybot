<?php
  $servername = "localhost";
  $username = "root";
  $password = "toor";
  $dbname = "smhackbot";

  // Create connection

  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
  }

  $sql = "INSERT INTO activity_history (timestamp,nfc_card_nfc_id) VALUES ('". date('Y-m-d G:i:s') . "','" . $_GET['id'] ."')";

  if ($conn->query($sql) === TRUE) {
     echo "New record created successfully";
  } else {
     echo "Error: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
?>
