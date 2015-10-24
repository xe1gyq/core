#!/usr/bin/python

import ConfigParser
import re
import speech_recognition as sr

from os import path

class xSpeechRecognition(object):

    def __init__(self):
        pass
    
    def setup(self):
        self.conf = ConfigParser.ConfigParser()
        self.path = "configuration/credentials.config"
        self.conf.read(self.path)
        appid=self.conf.get("wolfram", "appid")

        WAV_FILE = "output/xvoice.wav"
        self.r = sr.Recognizer()
        with sr.WavFile(WAV_FILE) as self.source:
            self.audio = self.r.record(self.source)

    def recognize(self):
        self.setup()
        try:
            from pprint import pprint
            print("Google Speech Recognition results:")
            pprint(self.r.recognize_google(self.audio, show_all=True))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":

    xs = xSpeechRecognition()
    xs.recognize()

# End of File
