#!/usr/bin/perl

use LWP::UserAgent;
use CGI;
use JSON::PP;

$cgi = CGI::new();

require './config.cgi';

my $token = $cgi->http('X-Auth-Token');

if( $token ne $APPLICATION_PASSWORD ) {
  print "Status: 401 Unauthorized\n";
  print "Content-Type: application/json\n\n";

  print "{\"result\": false, \"error\": \"Unauthorized. Confirm password again\"}";

  exit;
}

my $browser = LWP::UserAgent->new(
  agent => "DiscordBot ($WORKING_URL, $DISCORD_API_VERSION)"
);

my $response = $browser->post(
  $DISCORD_WEBHOOK,
  Content => decode_json($cgi->param('POSTDATA'))
);

if($response->content) {
  my $message = $response->content;
  print "Status: 406 Not Acceptable\n";
  print "Content-Type: application/json\n\n";

  print $message;

  exit;
} else {
  print "Status: 200 OK\n";
  print "Content-Type: text/plain\n\n";
}

exit;

