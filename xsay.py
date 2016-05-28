#!/usr/bin/python

import os
import subprocess

def say(language, message):

    if language is "english":
         language = "en-us"
    if language is "espanol":
         language = "es-mx"

    directorycurrent = os.path.dirname(os.path.realpath(__file__))
    voicerss = directorycurrent + '/voicerss.sh'
    command = [voicerss, language, message]
    proc = subprocess.call(command)

if __name__ == "__main__":

    say("english", "Hello World of Text To Speech via Voice RSS")
    say("espanol", "Hola Mundo Infraestructura de Texto a Voz")

# End Of File
