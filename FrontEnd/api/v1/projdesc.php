

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
 $crateid = $data1['uid'];
        $qty = $data1['module'];
        $len = $data1['moduleid'];
        $height = $data1['description'];
       print_r($crateid);
	    print_r($qty);
		 print_r($len);
		  print_r($height);
if($crateid!==''){

if($qty!==''){
$insert = "INSERT INTO status_tracker.project (module, moduleno, module_descripton,uid)
VALUES ('$qty','$len','$height',$crateid)";
}
if ($conn->query($insert) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
}



}


mysqli_close($conn);

?> 