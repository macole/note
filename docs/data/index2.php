<?php
//radiko player
//http://www.nakatayuki.com/


if(isset($_GET['id'])){

	$id = $_GET['id'];
	if($id=="stop"){
		exec("killall mplayer");
	}else if($id=="CCL"){
		exec("killall mplayer");
		exec("play_radiko.sh CCL", $e);
	}else if($id=="802"){
		exec("killall mplayer");
		exec("play_radiko.sh 802", $e);
	}else if($id=="ABC"){
		exec("killall mplayer");
		exec("play_radiko.sh ABC", $e);
	}else if($id=="MBS"){
		exec("killall mplayer");
		exec("play_radiko.sh MBS", $e);
	}else if($id=="OBC"){
		exec("killall mplayer");
		exec("play_radiko.sh OBC", $e);
	}else if($id=="RN1"){
		exec("killall mplayer");
		exec("play_radiko.sh RN1", $e);
	}else if($id=="RN2"){
		exec("killall mplayer");
		exec("play_radiko.sh RN2", $e);
	}else if($id=="CRK"){
		exec("killall mplayer");
		exec("play_radiko.sh CRK", $e);
	}else if($id=="KISSFMKOBE"){
		exec("killall mplayer");
		exec("play_radiko.sh KISSFMKOBE", $e);
	}else if($id=="HOUSOU-DAIGAKU"){
		exec("killall mplayer");
		exec("play_radiko.sh HOUSOU-DAIGAKU", $e);
	}
}
?>
<html>
<head>
<meta name="viewport" content="width=device-width">
</head>
<body>
<p><a href="index.php?id=stop">stop</a></p>
<ul>
<li><a href="index.php?id=802">FM 802</a></li>
<li><a href="index.php?id=CCL">FM COCOLO</a></li>
<li><a href="index.php?id=ABC">ABC Radio</a></li>
<li><a href="index.php?id=MBS">MBS Radio</a></li>
<li><a href="index.php?id=OBC">OBC Radio Osaka</a></li>
<li><a href="index.php?id=RN1">Radio NIKKEI 1</a></li>
<li><a href="index.php?id=RN2" >Radio NIKKEI2</a></li>
<li><a href="index.php?id=CRK" >CRK Radio Kansai</a></li>
<li><a href="index.php?id=KISSFMKOBE" >Kiss FM KOBE</a></li>
<li><a href="index.php?id=HOUSOU-DAIGAKU" >HOUSOU DAIGAKU</a></li>
</ul>
</body>
</html>