# Credentials

```sh
    $ nano core/configuration/credentials.config
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

    # WolframAlpha
    #
    # Go to developer.wolframalpha.com/ and sign up
    # Get your App Id under My Apps > Get an AppID 
    [wolframalpha]
    appid = 
    
    # PlotLy
    #
    # Go to https://plot.ly and sign up
    # Get your Username and API Key under Settings -> API Settings -> API
    # Get 3 Stream Tokens under Settings -> API Settings -> Streaming API -> Generate Token
    [plotly]
    username = 
    apikey = 
    streamtokena = 
    streamtokenb = 
    streamtokenc = 
    streamtokend = 
    
    # VoiceRss
    #
    # Go to www.voicerss.org and sign up
    # Go to API -> Get API Key
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
    [mashape]
    mashapekey = 
    
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
    
    # End of File
```

```sh
    $ nano core/configuration/voicerss.ak
```

```sh
    $ nano core/configuration/voicerss.mk
```

```sh

    $ ls core/configuration/
    credentials.config  voicerss.ak  voicerss.mk
```

