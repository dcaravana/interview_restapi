<?php
require_once(__DIR__ . '/SwaggerClient-php/autoload.php');

$config = new Swagger\Client\Configuration();
$config->setHost('http://127.0.0.1:8000');
$config->setDebug(false);
$config->setUsername('admin');
$config->setPassword('admin001');
$apiClient = new Swagger\Client\ApiClient($config);
$api_instance = new Swagger\Client\Api\CommentsApi($apiClient);
$api_instance_users = new Swagger\Client\Api\UsersApi($apiClient);


// users list
try {
    $users = $api_instance_users->usersList();
    echo 'users '. count($users) ."\n";
    foreach ($users as $user) {
      printf("%s\n", $user->username);
    }
} catch (Exception $e) {
    echo 'Exception when calling UsersApi->usersList: ', $e->getMessage(), PHP_EOL;
}
echo "\n";


// comments create
try {
    $data = new \Swagger\Client\Model\Data(array(
      'sku' => uniqid(),
      'content' => 'This is an incredibly positive message!'
    )); // \Swagger\Client\Model\Data | 
    $api_instance->commentsCreate($data);
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsCreate: ', $e->getMessage(), PHP_EOL;
}


// comments list
try {
    $comments = $api_instance->commentsList();
    echo 'comments '. count($comments) ."\n";
    foreach ($comments as $comment) {
      printf("%s, %s, %s\n", $comment->sku, $comment->content,
        $comment->tone_is_positive ? 'true' : 'false');
    }
} catch (Exception $e) {
    echo 'Exception when calling CommentsApi->commentsList: ', $e->getMessage(), PHP_EOL;
}
