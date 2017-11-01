<?php
//start session
session_start();

// Include config file and twitter PHP Library by Abraham Williams (abraham@abrah.am)
include_once("config.php");
include_once("inc/twitteroauth.php");
$bg="pattern.jpg";
?>
<!DOCTYPE html>
<html lang="en">
<head>
<!--	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
	!--><title>Login with Twitter </title>
    <style type="text/css">
	.wrapper{width:600px; margin-left:auto;margin-right:auto;}
	.welcome_txt{
		margin: 30px;
		background-color:#08A089;<!--#A0A09D!;!-->
		padding: 20px;
	<!--#font-family:arial;!-->
		border: #D6D6D6 solid 1px;
		-moz-border-radius:7px;
		-webkit-border-radius:7px;
		border-radius:7px;
		color:#F7F8F9;
		font-family:Verdana, sans-serif;
		
		height:50px;
	}
	.tweet_box{
		margin: 20px;
		background-color:#08A089;
		padding: 10px;
		border: #FFF0DD solid 1px;
		-moz-border-radius:5px;
		-webkit-border-radius:5px;
		border-radius:5px;
	}
	.tweet_box textarea{
		width: 500px;
		border: #A0A09D solid 1px;
		-moz-border-radius:5px;
		-webkit-border-radius:5px;
		border-radius:5px;
	}
	.tweet_list{
		margin: 20px;
		padding:20px;
		background-color: #08A089  ;
		border: #CBECCE solid 1px;
		-moz-border-radius:5px;
		-webkit-border-radius:5px;
		border-radius:5px;
	}
	.tweet_list ul{
		padding: 0px;
		font-family: verdana , sans-serif;
		font-size: 12px;
		color:#AED6F1  ; <!--#5C5C5C;!-->
	}
	.tweet_list li{
		border-bottom: #AED6F1  dashed 1px;
		list-style: none;
		padding: 5px;
	}
	
.long-shadow {
  display: inline-block;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  padding: 45px;
  border: none;
  background:#0B3B39;
  font: normal 60px/1 "Fredoka One", Helvetica, sans-serif;
  color: rgba(255,255,255,1);
  text-align: center;
  -o-text-overflow: clip;
  text-overflow: clip;
  text-shadow: 3px 3px 0 #0199d9 , 4px 4px 0 #0199d9 , 5px 5px 0 #0199d9 , 6px 6px 0 #0199d9 , 7px 7px 0 #0199d9 , 8px 8px 0 #0199d9 , 9px 9px 0 #0199d9 , 10px 10px 0 #0199d9 , 11px 11px 0 #0199d9 , 12px 12px 0 #0199d9 , 13px 13px 0 #0199d9 , 14px 14px 0 #0199d9 , 15px 15px 0 #0199d9 , 16px 16px 0 #0199d9 , 17px 17px 0 #0199d9 , 18px 18px 0 #0199d9 , 19px 19px 0 #0199d9 , 20px 20px 0 #0199d9 ;
}
.myButton {
	background-color:#A2D9CE  ;
	-moz-border-radius:28px;
	-webkit-border-radius:28px;
	border-radius:28px;
	border:1px solid <!--#18ab29;!-->
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:17px;
	padding:16px 31px;
	text-decoration:none;
	text-shadow:0px 1px 0px #2f6627;
	padding:absolute;
	left:30px;
}
.myButton:hover {
	background-color:#97B0AC;
}
.myButton:active {
	position:relative;
	top:1px;
	left-margin=-30px;
body{
	background-image:url('post_67_13.png');
}
 
	</style>
</head>
<body bgcolor='#D6DBDF'>

	
<?php
    
	if(isset($_SESSION['status']) && $_SESSION['status'] == 'verified') 
	{
		//Retrive variables
		$screen_name 		= $_SESSION['request_vars']['screen_name'];
		$twitter_id			= $_SESSION['request_vars']['user_id'];
		$oauth_token 		= $_SESSION['request_vars']['oauth_token'];
		$oauth_token_secret = $_SESSION['request_vars']['oauth_token_secret'];
	
		//Show welcome message
		#echo '<div class="long-shadow">Welcome <strong>'.$screen_name.'</strong> (Twitter ID : '.$twitter_id.'). <a href="logout.php?logout">Logout</a>!</div>';
		echo '<div class="welcome_txt">Welcome <strong>'.$screen_name.'</strong> (Twitter ID : '.$twitter_id.').</div>';
		#echo'<div button type="button" class="myButton" float="right"/><a href="logout.php?logout">Logout</a></div>';
		$connection = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, $oauth_token, $oauth_token_secret);
		echo'<button type="button" class="myButton"/><a href="animal.php">Animal</a></button>';  
		echo'<button type="button" class="myButton"  /><a href="women.php">Women Welfare</a></button>';
		echo'<button type="button" class="myButton"/><a href="health.php">Health</a></button>';
		echo'<button type="button" class="myButton"/><a href="oldage.php">Old_AGE</a></button>';
		echo'<button type="button" class="myButton"/><a href="child.php">Child Care</a></button>';
		//If user wants to tweet using form.
		if(isset($_POST["updateme"])) 
		{
			//Post text to twitter
			$my_update = $connection->post('statuses/update', array('status' => $_POST["updateme"]));
			die('<script type="text/javascript">window.top.location="index.php"</script>'); //redirect back to index.php
		}
		
		//show tweet form
		echo '<div class="tweet_box">';
		echo '<form method="post" action="index.php"><table width="200" border="0" cellpadding="3">';
		echo '<tr>';
		echo '<td><textarea name="updateme" cols="60" rows="4"></textarea></td>';
		echo '</tr>';
		echo'<tr>';
		echo '<td><input type="submit"  class="myButton" value="Tweet" /></td>';
		echo '</tr></table></form>';
		echo '</div>';
		
		//Get latest tweets
		$my_tweets = $connection->get('statuses/user_timeline', array('screen_name' => $screen_name, 'count' => 5));
		
		echo '<div class="tweet_list"><strong>Latest Tweets : </strong>';
		echo '<ul>';
		foreach ($my_tweets  as $my_tweet) {
			echo '<li>'.$my_tweet->text.' <br />-<i>'.$my_tweet->created_at.'</i></li>';
		}
		echo '</ul></div>';
			
			echo'<div button type="button" class="myButton" float="right"/><a href="logout.php?logout">Logout</a></div>';
	}else{
		
		//Display login button
		echo'<link href="https://fonts.googleapis.com/css?family=Lato:400,300,100,700,900" rel="stylesheet" type="text/css">
	<div class="inset-text-effect">NGO HELPERS</div>
	<ul>
        <li><a href="info.php"  class ="active" target="_blank">ABOUT US</a></li>
        <li><a href="#contact">CONTACT</a></li>
		
      </ul>
      
      </div>
	  <style type=text/css>
	 ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color:#73C6B6   ;
}

li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

a:hover:not(.active) {
    background-color: #D0ECE7  ;
}

.active {
background-color:#16A085;
}
</style>
<link async href="http://fonts.googleapis.com/css?family=Aladin" data-generated="http://enjoycss.com" rel="stylesheet" type="text/css"/>
<style type=text/css>
.inset-text-effect {
   margin-bottom:20px;
   margin-top:10px;
  display: inline-block;
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  border: #16A085;
  font: normal 70px/1 "Aladin", Helvetica, sans-serif;
  color: #16A085;
  text-align: center;
  text-transform: normal;
  -o-text-overflow: clip;
  text-overflow: clip;
  white-space: pre;
  text-shadow: 1px 1px 0 rgba(140,140,140,0.6) , -1px -1px 1px rgba(0,0,0,0.67) ;
}
</style>

    <style>
	
	body{
background-color:#D7DBDD ;

  background-position: center top;
  background-size: cover;
  margin: 0;
}
html, body {
  min-height: 100%;
  display: flex;
  flex-direction: column;
  font-weight: 300;
  line-height: 1.5;
}
h1, h2, h3 {
	margin: 0px;
	padding: 0px;
	text-transform: uppercase;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	color: #16A085;
         
}

h1 {
	font-size: 2em;
        text-transform: uppercase;
}

h2 {
	font-size: 2.4em;
}

h3 {
	font-size: 1.6em;
}


a {
  color: #204156;
  text-decoration: none;
}
	</style>
	
		<img class="img1"src="ngo.jpg"/>
	  <a href="process.php"><img class="btnimg" src="sign-in-with-twitter.png" width="250" height="70" border="0" /></a>
	  <style type=text/css>
	   .img1{
	
    border: 7px solid #16A085;
    padding: 20px; 
    width: 1150px;
    height: 600px; 
	margin-left:130px;
	margin-right:70px;
	margin-top:0px;
	
	  } 
	  .btnimg{
	  
	margin-left:630px;
	margin-right:470px;
	margin-top:20px;
	margin-bottom:20px;
	
	  }
	  </style>';
	  
	 
     
  
	
      
    
   
	  
	 
     
  
	}

	 ?> 
</body>
</html>