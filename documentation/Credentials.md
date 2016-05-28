# Credentials

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
  
# VoiceRss
#
# Go to www.voicerss.org and sign up
# Go to API -> Get API Key
# 
# apikey = voicerss.ak
# 
[voicerss]
apikey = 

# Mashape
#
# Go to market.mashape.com and sign up
# Search for VoiceRss API and click on it
# Copy your VoiceRss API Key and paste under "URL PARAMETERS key QUERY AUTH" field
# Fill out Form Encoded Parameters and Test EndPoint using Curl method
# Copy the generated Mashape Key
#
# apikey = voicerss.mk
# 
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
