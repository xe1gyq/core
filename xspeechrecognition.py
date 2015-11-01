#!/usr/bin/python

import ConfigParser
import json
import re
import speech_recognition as sr

from os import path

class xSpeechRecognition(object):

    def __init__(self, engine='google', wavfile='output/xvoice.wav'):
        self.engine = engine
        self.wavfile = wavfile
    
    def setup(self):
        self.r = sr.Recognizer()
        with sr.WavFile(self.wavfile) as self.source:
            self.audio = self.r.record(self.source)

    def fileset(self, wavfile):
        self.wavfile = wavfile

    def recognize(self):
        self.setup()
        if self.engine == 'google':
            try:
                from pprint import pprint
                print("Google Speech Recognition results:")
                return self.r.recognize_google(self.audio, show_all=False)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

if __name__ == "__main__":

    xs = xSpeechRecognition()
    print xs.recognize()

# End of File