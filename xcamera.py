#!/usr/bin/python

import commands
import logging
import os
import pygame
import pygame.camera

class xCamera(object):

    def __init__(self):

        self.directorycurrent = os.path.dirname(os.path.realpath(__file__))
        self.directoryoutput = self.directorycurrent + '/output/'
        self.picturepygame = self.directoryoutput + '/camerapygame.jpg'
        self.picturefswebcam = self.directoryoutput + '/camerafswebcam.jpg'


    def __del__(self):
        pass

    def filepath(self):
        return self.picturepygame

    def setup(self):
        try:

            pygame.camera.init()
            self.mypicture = pygame.camera.Camera("/dev/video0",(1280,720))

            self.fswebcam = 'fswebcam'
            self.fswebcamarguments = ' -r 1280x720 -s brightness=65% -s Contrast=50% -s Gamma=100% --jpeg 100 --no-banner '
            self.fswebcamcommand = self.fswebcam + self.fswebcamarguments + self.picturefswebcam

        except:
            print 'Camera Error'

    def capture(self):

        self.setup()

        self.mypicture.start()
        image = self.mypicture.get_image()
        pygame.image.save(image, self.picturepygame)
        self.mypicture.stop()

        status, output = commands.getstatusoutput(self.fswebcamcommand)

if __name__ == "__main__":

        idCamera = xCamera()
        idCamera.capture()

# End of File
