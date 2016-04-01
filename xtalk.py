#!/usr/bin/python

import os
import subprocess

def xtalk(language, message):

    directorycurrent = os.path.dirname(os.path.realpath(__file__))
    #voicerss = directorycurrent + 'core/voicerss.sh'
    voicerss = 'core/voicerss.sh'
    print voicerss
    command = [voicerss, language, message]
    proc = subprocess.call(command)

if __name__ == "__main__":

    xtalk("en-us", "Hello World of Text To Speech via Voice RSS")

# End Of File
