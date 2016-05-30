#!/bin/sh

apt-get install python-pip python-dev python-opencv curl mpg123 python-pygame libxft-dev
opkg install python-opencv python-dev fswebcam alsa-utils mpg123 espeak libxft-dev libpng-dev 
opkg install libjack
opkg install --nodeps jack-dev 
opkg install libportaudio-dev
pip install wit SpeechRecogntion paho-mqtt wolframalpha matplotlib twython pyaudio --target /home/root/
