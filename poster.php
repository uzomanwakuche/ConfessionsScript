<?php
require_once __DIR__ . '/vendor/autoload.php'; // change path as needed


$facebook_secret = json_decode(file_get_contents('facebook_secret.json'), true);

//Pulls secret key API info from facebook_secret.json and passes it into FB object
$fb = new \Facebook\Facebook($facebook_secret);

try {
  
  //Reads csv file
  $file = fopen('week.csv', 'r'); 
  
  while (($line = fgetcsv($file)) !== FALSE) {
    $response = $fb->post('/2156420374634389/feed',
              array (
                'message' =>$line[2] ,
                'scheduled_publish_time' => $line[3] ,
                'published' => 'false'
              ));
  }

} catch(\Facebook\Exceptions\FacebookResponseException $e) {
  // When Graph returns an error
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(\Facebook\Exceptions\FacebookSDKException $e) {
  // When validation fails or other local issues
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
//2156420374634389/feed?message=Test
//$me = $response->getGraphUser();
//echo 'Logged in as ' . $me->getName();
?>
