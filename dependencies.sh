#!/bin/sh

apt-get install python-pip python-dev python-opencv curl mpg123 python-pygame libxft-dev
opkg install python-dev fswebcam alsa-utils mpg123 espeak libxft-dev libpng-dev
pip install SpeechRecogntion paho-mqtt wolframalpha matplotlib twython --target /home/root/
