<?php

$apiHost = getenv("API_HOST");

$topic = $_GET['topic'];
$from = $_GET['from'];
$to = $_GET['to'];

$queryArguments = "$topic?from=$from&to=$to";

$apiRoot = "http://localhost:8080/$queryArguments";

$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'GET'
    ),
);

$context  = stream_context_create($options);
$result = file_get_contents($apiRoot, false, $context);

echo $result;
