#!/usr/bin/python

import time
import pyupm_buzzer as upmBuzzer

def xanswer(bus, valid):

    buzzer = upmBuzzer.Buzzer(bus)

    if valid:
        print buzzer.playSound(upmBuzzer.DO, 1)
        time.sleep(.2)
        print buzzer.playSound(upmBuzzer.DO, 1)        
    else:
        print buzzer.playSound(upmBuzzer.DO, 1)

if __name__ == "__main__":

    xanswer(5, False)

# End of File
