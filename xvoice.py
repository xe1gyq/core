#!/usr/bin/python

import commands
import os
import subprocess
import time

class xVoice(object):

    def __init__(self, voicefile="voice.wav"):
        self.directorycurrent = os.path.dirname(os.path.realpath(__file__))
        self.directoryoutput = self.directorycurrent + '/output/'
        self.voicefile = self.directoryoutput + voicefile
        self.filename = "output/xvoice.wav"
        self.proc = None

    def filenameset(self, voicefile):
        self.voicefile = voicefile

    def filenameget(self, voicefile):
        return self.voicefile

    def recordstart(self):
        args = ['arecord', '-D', 'plughw:1,0', '-t', 'wav', '-f', 'S16_LE', '-r', '48000', self.voicefile]
        #args = ['arecord', '-t', 'wav', '-f', 'S16_LE', '-r', '48000', self.filename]
        proc = subprocess.Popen(args)
        print "PID:", proc.pid
        return proc

    def recordstop(self, proc):
        proc.kill()

    def record(self):
        time.sleep(1)
        proc = self.recordstart()
        time.sleep(5)
        self.recordstop(proc)

    def play(self):
        status, output = commands.getstatusoutput("aplay " + self.voicefile)
        print output

    def erase(self):
        status, output = commands.getstatusoutput("rm " + self.voicefile)

if __name__ == "__main__":

    idVoice = xVoice()
    idVoice.record()
    idVoice.play()

    pid = idVoice.recordstart()
    time.sleep(5)
    idVoice.recordstop(pid)
    idVoice.play()

# End of File
