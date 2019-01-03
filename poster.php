<?php
require_once __DIR__ . '/vendor/autoload.php'; // change path as needed


$facebook_secret = json_decode(file_get_contents("facebook_secret.json"), true);

//Pulls API info from facebook_secret.json and converts into a list
$fb = new \Facebook\Facebook($facebook_secret);

try {

  // Get the \Facebook\GraphNodes\GraphUser object for the current user.
  // If you provided a 'default_access_token', the '{access-token}' is optional.
  $message = "Testing Testing";
  $response = $fb->post("/2156420374634389/feed?message={$message}");
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
