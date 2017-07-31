
<html>
<head>

<div class="long-shadow">Ready to help  twitter users</div>
<link async href="http://fonts.googleapis.com/css?family=Fredoka%20One" data-generated="http://enjoycss.com" rel="stylesheet" type="text/css"/>
<style type=text/css>
.long-shadow {
  display: inline-block;                                             <!--shadow=#0199d9!-->
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  padding: 45px;
  border: none;
  background:#08A089;
  font: normal 60px/1 "Fredoka One", Helvetica, sans-serif;
  color: rgba(255,255,255,1);
  text-align: center;
  -o-text-overflow: clip;
  text-overflow: clip;
  margin:0 auto;
  width:100%;
  text-shadow: 3px 3px 0 #A2D9CE  , 4px 4px 0 #A2D9CE , 5px 5px 0 #A2D9CE , 6px 6px 0 #A2D9CE , 7px 7px 0 #A2D9CE , 8px 8px 0  #A2D9CE , 9px 9px 0 #A2D9CE , 10px 10px 0 #A2D9CE, 11px 11px 0 #A2D9CE, 12px 12px 0 #A2D9CE , 13px 13px 0 #A2D9CE , 14px 14px 0 #A2D9CE , 15px 15px 0 #A2D9CE , 16px 16px 0 #A2D9CE, 17px 17px 0 #A2D9CE , 18px 18px 0 #A2D9CE , 19px 19px 0 #A2D9CE, 20px 20px 0 #A2D9CE ;
}
table, td {
   border: 1px solid #000000;
   align:center;
   width:50%;
   bgcolor:#2589D3;
   <!--cellspacing:"5";!-->
   table-layout:fixed;
}
<!--table.hovertable {
	font-family: verdana,arial,sans-serif;
	font-size:11px;
	color:#333333;
	border-width: 1px;
	border-color: #999999;
	border-collapse: collapse;
}
 th {
	background-color:#c3dde0;
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #a9c6c9;
}
table.hovertable tr {
	background-color:#d4e3e5;
}
table.hovertable td {
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #a9c6c9;
}
<!--p.padding{
	padding-left:3cm;
}
!-->

</style>
</head>
<body bgcolor='#D6DBDF'>
<?php
#<table align="center" style="margin: 0px auto;"></table>

echo "<html><body><table id='display' align='center'>\n\n";
#$f = fopen("USER_DATA.csv", "r");
$f=fopen("INTEREST_PERCENT_CHILD.csv","r");
$col=0;

$col1=6;
#$col2=1;
echo "<tr bgcolor='#16A085' >";
		echo"<th><h3>PROFILE_PIC</h3></td>";
		
		echo"<th>SCREEN_NAMES</td>";
		echo"<th>FOLLOW</td>";
		echo"</tr>";
while (!feof($f)) {
	      #echo "<table bgcolor='#E0F8F7' align='center' >";
	#echo"<thead>PROFILE_PIC</thead>";
        
		echo"<tr>";
		
        $username=fgetcsv($f)[$col];
        $link=fgetcsv($f)[$col1];	
		#echo"/$link/";
#		$id=fgetcsv($f)[$col2];
		
		#echo"<a href='index.php'>";
	
		
		/*$arraylenght=count($link1);
			for($x=0;$x<$arraylenght;$x++) 
			{
				if($line[$x]='ANIMAL')
				{
					
				
		
     
		
		
			#if($col1=="ANIMAL"){*/
          # echo"<th>IMAGE</th>";    
 #echo"<td <a href='https://twitter.com<screen_name='$username'>/profile_image?size=<mini|normal|bigger|original'></a></td>";		  
		echo"<td bgcolor='#A2D9CE'><img src=\"$link\" alt='twitter_image'>";
		  
		 # echo "<td>". htmlspecialchars($cell)[$col] . "</td>";
             echo "<td align='center' padding='2px' bgcolor='#A2D9CE'>\"$username\"</a></td>";//image2wbmp
		#	 echo"<td><a href='https://twitter.com/<\"$username\">/profile_image?size=<mini|normal|bigger|original'></a></td>";
		       
			   /*
			   <form class='follow ' id='follow_btn_form' action='/intent/follow?screen_name='$username' method='post'>
      <input type='hidden' name='authenticity_token value=f2e645564f77b9d8e9623f7056ec9f3afec2d897>
      <input type='hidden' name='screen_name'value='$username'>
        <input name='screen_name'type='hidden'value='$username'>
  <input name='tw_p' type='hidden' value='followbutton'>
  <input name='original_referer' type='hidden' value='https://publish.twitter.com/'>

      <input type='hidden' name='profile_id' value='$id'>*/
	  

    echo"<td padding='2px' bgcolor='#A2D9CE'> <button class='button' type='submit' >
        <b></b><strong>Follow<a href='https://twitter.com/intent/user?screen_name=$username' 
class='twitter-follow-button' data-show-count='false' data-size='large'>
Follow@'$username'</a>  
		
		</strong>
      </button>
    </td>";
			   #echo"<td><a href='https://twitter.com/TwitterDev' class='twitter-follow-button' data-show-count='false'>Follow @TwitterDev</a><script async src='//platform.twitter.com/widgets.js' charset='utf-8'></script>";
	echo"</a>";
        echo "</tr>\n";
		
#echo"</table>";
	  
			}
	  
			
fclose($f);
echo "\n</table></body></html>";
	  
# echo"https://twitter.com/<screen_name>/profile_image?size=<mini|normal|bigger|original>";
?>