#!/usr/bin/perl

use LWP::UserAgent;
use CGI;

$cgi = CGI::new();

require './config.cgi';

my $token = $cgi->http('X-Auth-Token');

if( $token ne $APPLICATION_PASSWORD ) {
  print "Status: 401 Unauthorized\n";
  print "Content-Type: application/json\n\n";

  print "{\"error\": \"Unauthorized. Confirm password again\"}";

  exit;
}

my $browser = LWP::UserAgent->new;
my $response = $browser->get(
  "https://discordapp.com/api/guilds/$DISCORD_GUILD_ID/threads/active",
  "Authorization" => "Bot $DISCORD_TOKEN",
  "User-Agent"=> "DiscordBot ($WORKING_URL, $DISCORD_API_VERSION)"
);

print "Status: 200 OK\n";
print "Content-Type: text/plain\n\n";

print $response->content;
exit;
exit;

