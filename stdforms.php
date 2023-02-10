<html>
    <body>
	<style>
	body{
		align:center;
		background-color:blue;
		color:pink;
	}
	</style>
	
        student details:<?php
         $H=$_POST['name1111'];
		 $age=$_POST['age'];
		 $g=$_POST['gender'];
         echo $H;
		 ?>
		 <br>
		 <?php
		 echo 'your age' ,$age;
		 ?>
		 <br>
		 <?php
		 echo 'your gender', $g;
?>
<br>
<?php
echo $_POST['email1111'];
?>
<br>

<?php if(isset($_POST['upload'])){
$image_name=$_FILES['image']['name'];
$image_type=$_FILES['image']['type'];
$image_size=$_FILES['image']['size'];
$image_tmp_name=$_FILES['image']['tmp_name'];
move_uploaded_file($image_tmp_name,"photos/$image_name");
echo "<img src='photos/$image_name' width='400' height='250'><br>";}