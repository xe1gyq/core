#!/usr/bin/python

import commands
import subprocess
import time

class xVoice(object):

    def __init__(self):
        self.filename = "output/xvoice.wav"
        self.proc = None

    def filenameset(self, filename):
        self.filename = filename

    def filenameget(self, filename):
        return self.filename

    def recordstart(self):
        args = ['arecord', '-D', 'plughw:1,0', '-t', 'wav', '-f', 'S16_LE', '-r', '48000', self.filename]
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
        status, output = commands.getstatusoutput("aplay " + self.filename)
        print output

    def erase(self):
        status, output = commands.getstatusoutput("rm " + self.filename)

if __name__ == "__main__":

    idVoice = xVoice()
    idVoice.record()
    idVoice.play()

    pid = idVoice.recordstart()
    time.sleep(5)
    idVoice.recordstop(pid)
    idVoice.play()

# End of File
