Introduction
==

## 

```sh
    $ cd
    $ mkdir project
    $ cd project
    $ git clone https://github.com/xe1gyq/core.git
    $ mkdir configuration
```

## Credentials

```sh
    $ nano configuration/credentials
```

```sh
    # IoTPy File Configuration
    
    # Go to https://plot.ly and sign up
    # Get your Username and API Key under Settings -> API Settings -> API
    # Get 3 Stream Tokens under Settings -> API Settings -> Streaming API -> Generate Token
    [plotly]
    username = 
    apikey = 
    streamtoken = 
    streamtokentx = 
    streamtokenrx = 
    
    # Go to dev.twitter.com and sign up
    # Go to Tools -> Manage Your Apps (Application Management)
    # Create a New Application and go to "Keys and Access Tokens" tab
    # Generate and get under Application Settings section
    # Consumer Key (API Key), Consumer Secret (API Secret)
    # Generate and get under Your Access Token section
    # Access Token and Access Token Secret
    # Give Access Level "Read and Write"
    [twitter]
    consumer_key = 
    consumer_secret = 
    access_token = 
    access_token_secret = 
    
    # Go to www.voicerss.org and sign up
    # Go to API -> Get API Key
    # 
    [voicerss]
    apikey = 

    # Go to market.mashape.com and sign up
    # Search for VoiceRss API and click on it
    # Copy your VoiceRss API Key and paste under "URL PARAMETERS key QUERY AUTH" field
    # Fill out Form Encoded Parameters and Test EndPoint using Curl method
    # Copy the generated Mashape Key
    [mashape]
    mashapekey = 
    
    # End of File
```

## Class xCamera

Take a picture from connected Camera through USB

```sh
    $ python core/xcamera.py
```

```Python
    from core.xcamera import xCamera

    idCamera = xCamera()
    idCamera.capture()
```

## Class xFaceRecognition

> Open Source Computer Vision. OpenCV is released under a BSD license and hence it’s free for both academic and commercial use. It has C++, C, Python and Java interfaces and supports Windows, Linux, Mac OS, iOS and Android. OpenCV was designed for computational efficiency and with a strong focus on real-time applications.

- [OpenCV Homepage](http://opencv.org/)

```sh
    $ python core/xfacerecognition.py
```

```Python
    from core.xfacerecognition import xFaceRecognition

    idFaceRecognition = xFaceRecognition(imageinput='in.jpeg', imageoutput='out.jpeg')
    idFaceRecognition.detect()
```

## Class xLcdRgb

> The RGB color model is an additive color model in which red, green, and blue light are added together in various ways to reproduce a broad array of colors. The name of the model comes from the initials of the three additive primary colors, red, green, and blue. [Wikipedia](https://en.wikipedia.org/wiki/RGB_color_model)

> A liquid-crystal display (LCD) is a flat panel display, electronic visual display, or video display that uses the light modulating properties of liquid crystals. Liquid crystals do not emit light directly. [Wikipedia](https://en.wikipedia.org/wiki/Liquid-crystal_display)

Set a specific color in the display and show a specific text

```sh
    $ python core/xlcdrgb.py
```

```Python
    from core.xlcdrgb import xLcdRgb
    
    idLcdRgb = xLcdRgb()
    while True:
        idLcdRgb.clear()
        idLcdRgb.setCursor(0,0)
        idLcdRgb.setText("Hello Lcd Rgb!")
        idLcdRgb.setColor("Red")
```

## Class xMqttPub

> MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport. It is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium.

- [MQTT Homepage](http://mqtt.org/)

```Python
    from core.xmqttpub import xMqttPub
    
    idMqtt = xMqttPub(server="test.mosquitto.org", port=1883)
    idMqtt.write("temp/random", "43")
```

## Class xPlotLy

> Plotly is an online analytics and data visualization tool, headquartered in Montreal, Quebec. Plotly provides online graphing, analytics, and stats tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST. Wikipedia. [Wikipedia](https://en.wikipedia.org/wiki/Plotly)

[PlotLy Homepage](https://plot.ly/)


```Python
    from core.xplotly import xPlotLy
    
    xPlotly = xPlotLy("Core PlotLy Random")
    counter = 0
    while True:
        xPlotly.graph(counter, random.random())
        counter += 1
        time.sleep(0.5)
```

### Class xSpeechRecognition

```Python
    from core.xspeechrecognition import xSpeechRecognition
    
    idSpeechRecognition = xSpeechRecognition()
    print idSpeechRecognition.recognize()
```

### Function xtalk

Uses VoiceRSS service through Mashape to enable Text To Speech Service

> Voice RSS provides free text-to-speech (TTS) online service and free TTS API with very fast and simple integration.

[VoiceRSS Homepage](http://www.voicerss.org/)

> Hundreds of thousands of developers rely on Mashape products for deliverying better APIs and Microservices.

[Mashape Homepage](https://www.mashape.com/)

```Python
    from core.xtalk import xtalk
    
    xtalk("en-us", "Hello World of Text To Speech via Voice RSS")
```

### Function xTwitter

> Twitter (/ˈtwɪtər/) is an online social networking service that enables users to send and read short 140-character messages called "tweets". [Wikipedia](https://en.wikipedia.org/wiki/Twitter)

[Twitter Homepage](https://twitter.com/)

```Python
    # Usage
    from core.xtweet import xTwitter
    
    idTwitter = xTwitter()
    idTwitter.tweet('#TheIoTLearningInitiative Testing Time', None)
```

### Class xVoice

```Python
    from core.xvoice import xVoice

    idVoice = xVoice()
    idVoice.record()
    idVoice.play()
```

### Class xWolfram

> Wolfram Alpha (also styled WolframAlpha and Wolfram|Alpha) is a computational knowledge engine[4] or answer engine developed by Wolfram Research. It is an online service that answers factual queries directly by computing the answer from externally sourced "curated data", rather than providing a list of documents or web pages that might contain the answer as a search engine might. [Wikipedia](https://en.wikipedia.org/wiki/Wolfram_Alpha)

[Wolfram Alpha Homepage](http://www.wolframalpha.com/)

```Python
    from core.xwolfram import xWolfram

    idWolfram = xWolfram()
    question = "What is the capital of Mexico"
    answer = idWolfram.question(question)
    print answer
```
