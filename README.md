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

    # Usage, Python
    from core.xcamera import xCamera
    xc = xCamera()
    xc.capture()

## Class xLcdRgb

Set a specific color in the display and show a specific text

    from core.xlcdrgb import xLcdRgb
    xlr = xLcdRgb()
    while True:
        xlr.clear()
        xlr.setCursor(0,0)
        xlr.setText("Hello Lcd Rgb!")
        xlr.setColor("Red")

## Class xPlotly

> Plotly is an online analytics and data visualization tool, headquartered in Montreal, Quebec. Plotly provides online graphing, analytics, and stats tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST.

[PlotLy Homepage](https://plot.ly/)



