#!/usr/bin/perl

use CGI;

# Create the CGI object
my $query = new CGI;

# Output the HTTP header
print $query->header ( );

# Capture the form results
my $fullname = $query->param("fullname")
my $email_address = $query->param("email");
my $message = $query->param("message");

# Filter the form results
$fullname = filter_field ( $fullname )
$email_address = filter_header_field ( $email_address );
$message = filter_field ( $message );

# Email the form results
open ( MAIL, "| /usr/lib/sendmail -t" );
print MAIL "From: $email_address\n";
print MAIL "To: info\@achievecare.ca\n";
print MAIL "Subject: Contact Form\n\n";
print MAIL "Fullname: $fullname\n";
print MAIL "$message\n";
print MAIL "\n.\n";
close ( MAIL );

# Functions for filtering user input

sub filter_field
{
  my $field = shift;
  $field =~ s/From://gi;
  $field =~ s/To://gi;
  $field =~ s/BCC://gi;
  $field =~ s/CC://gi;
  $field =~ s/Subject://gi;
  $field =~ s/Content-Type://gi;
  return $field;
}

sub filter_header_field
{
  my $field = shift;
  $field =~ s/From://gi;
  $field =~ s/To://gi;
  $field =~ s/BCC://gi;
  $field =~ s/CC://gi;
  $field =~ s/Subject://gi;
  $field =~ s/Content-Type://gi;
  $field =~ s/[\0\n\r\|\!\/\<\>\^\$\%\*\&]+/ /g;
  return $field;
}
