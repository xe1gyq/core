Core
==

## Script svoicerss.sh

Uses VoiceRSS service through Mashape to enable Text To Speech Service

> Voice RSS provides free text-to-speech (TTS) online service and free TTS API with very fast and simple integration.

[VoiceRSS Homepage](http://www.voicerss.org/)

> Hundreds of thousands of developers rely on Mashape products for deliverying better APIs and Microservices.

[Mashape Homepage](https://www.mashape.com/)

    # Usage, Shell
    voicerss.sh en-us "Hello World!"
    voicerss.sh es-mx "Hola Mundo!"

## Function xanswer

Allows to beep for True (2 tones) or False (1 tone)

    # Usage, Pyton
    from core.xanswer import xanswer
    xanswer(5, False)

## Class xCamera

Take a picture from connected Camera through USB

    # Usage
    from core.xcamera import xCamera
    xc = xCamera()
    xc.capture()

