#!/usr/bin/python

import subprocess

def xtalk(language, message):

    command = ['core/svoicerss.sh', language, message]
    proc = subprocess.call(command)

if __name__ == "__main__":

    xtalk("en-us", "hi")

# End Of File
