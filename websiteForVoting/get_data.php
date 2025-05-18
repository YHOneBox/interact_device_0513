<?php
header('Content-Type: application/json');

// 資料庫連接信息
$servername = "127.0.0.1:3306";
$username = "u141787484_1";
$password = "ETyh06241228";
$dbname = "u141787484_db";

// 創建連接
$conn = new mysqli($servername, $username, $password, $dbname);

// 檢查連接
if ($conn->connect_error) {
    echo json_encode(["status" => "Connection failed: " . $conn->connect_error]);
    exit();
}

// 獲取資料庫中的資料
$sql = "SELECT visitorId, groupNumber FROM heheinfo WHERE id = 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    echo json_encode(["status" => "success", "visitorId" => $row["visitorId"], "groupNumber" => $row["groupNumber"]]);
} else {
    echo json_encode(["status" => "error", "message" => "No data found"]);
}

$conn->close();
?>
