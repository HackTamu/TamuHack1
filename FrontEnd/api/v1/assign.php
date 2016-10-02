

<?php
echo "Hello World!";
$postdata = file_get_contents("php://input");
$request = json_decode($postdata,true);
print_r($request);


echo "Success";
$servername = "localhost";
$username = "root";
$password = "admin";

$conn = mysqli_connect($servername, $username, $password);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully";
foreach($request as $data1) 
{
 $crateid = $data1['assignename'];
        $qty = $data1['assignerid'];
        $len = $data1['module'];
        $height = $data1['moduleid'];
        $weight = $data1['startdate'];
$weight2 = $data1['enddate'];
if($crateid!==''){
$sql = "SELECT project_id FROM status_tracker.project where module='".$len."' and moduleno='".$height."'";
$result = $conn->query($sql);
$row = $result->fetch_assoc();
   echo "id: " . $row["project_id"]. " - Name: " . $row["project_id"]. " " . $row["project_id"]. "<br>";
 $sql1 = "SELECT uid FROM status_tracker.customers_auth where name='".$crateid."' ";
$result1 = $conn->query($sql1);
$row1 = $result1->fetch_assoc();
     
 //$sql2 = "SELECT id FROM status_tracker.senior_leader where first_name='".$qty."' ";
//$result2 = $conn->query($sql2);
//$row2 = $result2->fetch_assoc();
 $deliverydate = json_encode($weight2);
   $deliverydate = str_replace('"','\'',$deliverydate);
 $startdate = json_encode($weight);
   $startdate = str_replace('"','\'',$startdate);
if($qty!==''){
$insert = "INSERT INTO status_tracker.assigned_to (project_id, uid, uid1,date_assigned,date_end)
VALUES (".$row["project_id"].",$qty,".$row1["uid"].",$startdate,$deliverydate)";
}
if ($conn->query($insert) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
}

print_r($qty);

}
$sql = "SELECT uid, l_name FROM status_tracker.customers_auth";
$result = $conn->query($sql);
 while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["first_name"]. " " . $row["last_name"]. "<br>";
    }

mysqli_close($conn);

?> 
