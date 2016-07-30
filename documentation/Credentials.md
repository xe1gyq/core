# Credentials

# VoiceRss

> The Voice RSS Text-to-Speech (TTS) API allows conversion of textual content to speech easier than ever. Just connect to our Text-to-Speech (TTS) API with a few lines of code and get verbal representation of a textual content. For converting text to speech you don’t need special hardware to care about intensive use of CPU and memory during conversion operations. [Homepage](http://www.voicerss.org/)

1. [Registration](http://www.voicerss.org/registration.aspx)
   - First Name: 
   - Last Name: 
   - Company Name:
   - Email: 
   - Password:
   - Confirm Password:
   - Site URL:
   - Code Protection: 
   - Discount Coupon: 
   - Register ...
2. [Personel](http://www.voicerss.org/personel)
3. Generate New API Key
   - API Key: -------------------
   - Current Plan: Free
   - Update ...

# Mashape

> Powering APIs, Microservices and Serverless Software. Developers & DevOps rely on Mashape products to deliver better APIs & Microservices [Homepage](https://www.mashape.com/)

- [Unirest](http://unirest.io/python)

1. [Sign Up / Register](https://market.mashape.com/register
   - Username
   - Email
   - Password
   - Create Account
3. [Mashape Dashboard](https://market.mashape.com/dashboard)
4. Add New Application. Mashape allows you to consume and monitor APIs in your Application, giving you a one stop shop for monitoring, payments, and management.
   -  Application Name: NuupXe
5. Add Another API: Explore Market Place
   -  Search: VoiceRss
   -  https://market.mashape.com/voicerss/text-to-speech-1

## Test Endpoints

Convert text to speech via HTTP POST
> Converts textual content to audio content

1. URL Parameters
  - key: -------------------
2. Request Headers
  - X-Mashape-Key: Default Application
3. Test Endpoint ...

```sh
root@edison:~/myproject# nano core/configuration/credentials.config
```

```sh
# IoTPy File Configuration

# Twitter
#
# Go to dev.twitter.com and sign up
# Go to Tools -> Manage Your Apps (Application Management)
# Create a New Application and go to "Keys and Access Tokens" tab
# Generate and get under Application Settings section:
#  Consumer Key (API Key), Consumer Secret (API Secret)
# Generate and get under Your Access Token section
#  Access Token and Access Token Secret
# Give Access Level "Read and Write"
[twitter]
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 
  
[voicerss]
apikey = 

[mashape]
mashapekey = 

# WolframAlpha
#
# Go to developer.wolframalpha.com/ and sign up
# Get your App Id under My Apps > Get an AppID 
[wolframalpha]
appid = 

# Google
#
[google]
api_key = 
    
# Gmail
#
[gmail]
username = 
password = 
    
# Telegram
#
[telegram]
token = 

# Wit
# 
[wit]
accesstoken=

# End of File
```

```sh
root@edison:~/myproject# nano core/configuration/voicerss.ak

[Write Voicerss ApiKey]

```

```sh
root@edison:~/myproject# nano core/configuration/voicerss.mk

[Write Mashape MashapeKey]

```

```sh
root@edison:~/myproject# ls core/configuration/
credentials.config  haarcascade_frontalface_alt.xml  voicerss.ak  voicerss.mk
```

## Google Credentials

```sh
root@edison:~/myproject# export GOOGLE_APPLICATION_CREDENTIALS=<path_to_service_account_file>
```
