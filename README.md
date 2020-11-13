# Server checker

## About cript
This script sends an SMS if the site is unavailable

## How it works
There only two functions: "send_sms" , "check_server".
The first function sent sms by Twilio. Numbers to send and receive are taken from .env file. 
If message was not sent then notification is displayed.
The second function check server availability. If it is not avalibale function sent sms by first function. 
