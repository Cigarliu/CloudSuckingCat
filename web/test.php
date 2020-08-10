<?php

$action = $_GET["action"];

function udpGet($sendMsg = '', $ip = 'a.comeboy.cn', $port = '1234'){

  $handle = stream_socket_client("udp://{$ip}:{$port}", $errno, $errstr);

  if( !$handle ){

    die("ERROR: {$errno} - {$errstr}\n");

  }

  fwrite($handle, $sendMsg);
      fclose($handle);

}

udpGet($action);

?>