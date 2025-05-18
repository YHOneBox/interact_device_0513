<?php
header('Content-Type: application/json');

$input = file_get_contents('php://input');
$data = json_decode($input, true);

if (isset($data['visitorId']) && isset($data['groupNumber'])) {
    $visitorId = $data['visitorId'];
    $groupNumber = $data['groupNumber'];

    // 資料庫連接信息
    
    $servername = "127.0.0.1:3306";
    $username = "u141787484_1";
    $password = "ETyh06241228";
    $dbname = "u141787484_db";

    // 創建連接
    $conn = new mysqli($servername, $username, $password, $dbname);

    // 檢查連接
    if ($conn->connect_error) {
        die(json_encode(["status" => "Connection failed: " . $conn->connect_error]));
    }

    // 更新資料庫
    $sql = "UPDATE heheinfo SET visitorId = ?, groupNumber = ? WHERE id = 1";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $visitorId, $groupNumber);

    if ($stmt->execute()) {
        echo json_encode(["status" => "Data updated successfully"]);
    } else {
        echo json_encode(["status" => "Error updating data: " . $stmt->error]);
    }

    $stmt->close();
    $conn->close();
} else {
    echo json_encode(["status" => "Invalid input"]);
}
?>
