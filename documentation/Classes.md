# Classes

## xCamera

__Additional hardware required!__ Take a picture from connected Camera through USB

```sh
    $ python core/xcamera.py
```

```Python
    from core.xcamera import xCamera

    idCamera = xCamera()
    idCamera.capture()
```

## xFaceRecognition

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

## xLcdRgb

> The RGB color model is an additive color model in which red, green, and blue light are added together in various ways to reproduce a broad array of colors. The name of the model comes from the initials of the three additive primary colors, red, green, and blue. [Wikipedia](https://en.wikipedia.org/wiki/RGB_color_model)

> A liquid-crystal display (LCD) is a flat panel display, electronic visual display, or video display that uses the light modulating properties of liquid crystals. Liquid crystals do not emit light directly. [Wikipedia](https://en.wikipedia.org/wiki/Liquid-crystal_display)

__Additional hardware required!__ Set a specific color in the display and show a specific text. 


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

## xMqttPub

> MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport. It is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium.

- [MQTT Homepage](http://mqtt.org/)

```sh
    $ python core/xmqttpub.py
```

```Python
    from core.xmqttpub import xMqttPub
    
    idMqtt = xMqttPub(server="test.mosquitto.org", port=1883)
    idMqtt.write("temp/random", "43")
```


### xSpeechRecognition

__Additional hardware required!__ 

```sh
root@edison:~# vi ~/.asoundrc
```

```sh
pcm.!default {
    type plug
       slave {
           pcm "hw:3,0"
       }
}
ctl.!default {
    type plug
        slave {
           pcm "hw:2,0"
       }
}
```

```sh
    $ python core/xspeechrecognition.py
```

```Python
    from core.xspeechrecognition import xSpeechRecognition
    
    idSpeechRecognition = xSpeechRecognition()
    print idSpeechRecognition.recognize()
```

### xTalk

__Additional hardware required!__ Uses VoiceRSS service through Mashape to enable Text To Speech Service

> Voice RSS provides free text-to-speech (TTS) online service and free TTS API with very fast and simple integration.

[VoiceRSS Homepage](http://www.voicerss.org/)

> Hundreds of thousands of developers rely on Mashape products for deliverying better APIs and Microservices.

[Mashape Homepage](https://www.mashape.com/)

```sh
    $ python core/xtalk.py
```

```Python
    from core.xtalk import xtalk
    
    xtalk("en-us", "Hello World of Text To Speech via Voice RSS")
```

### xTwitter

> Twitter (/ˈtwɪtər/) is an online social networking service that enables users to send and read short 140-character messages called "tweets". [Wikipedia](https://en.wikipedia.org/wiki/Twitter)

[Twitter Homepage](https://twitter.com/)

```sh
    $ python core/xtwitter.py
```

```Python
    from core.xtweet import xTwitter
    
    idTwitter = xTwitter()
    idTwitter.tweet('#TheIoTLearningInitiative Testing Time', None)
```

### xVoice

__Additional hardware required!__ 

```sh
    $ python core/xvoice.py
```

```Python
    from core.xvoice import xVoice

    idVoice = xVoice()
    idVoice.record()
    idVoice.play()
```

### xWolfram

> Wolfram Alpha (also styled WolframAlpha and Wolfram|Alpha) is a computational knowledge engine[4] or answer engine developed by Wolfram Research. It is an online service that answers factual queries directly by computing the answer from externally sourced "curated data", rather than providing a list of documents or web pages that might contain the answer as a search engine might. [Wikipedia](https://en.wikipedia.org/wiki/Wolfram_Alpha)

[Wolfram Alpha Homepage](http://www.wolframalpha.com/)

```Python
from core.xwolfram import xWolfram

idWolfram = xWolfram()                                                      
print idWolfram.question("What is the capital of Mexico")                   
```

```sh
root@edison:~/myproject# python core/xwolfram.py                                
Mexico City Distrito Federal Mexico                                             
root@edison:~/myproject# 
```
