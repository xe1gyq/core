#!/usr/bin/python

import cv2
import os
import sys

class xFaceRecognition(object):

    def __init__(self, imageinput="photo.jpeg", imageoutput="faces.jpeg"):
        self.directorycurrent = os.path.dirname(os.path.realpath(__file__))
        self.directoryfiles = self.directorycurrent + '/files/'
        self.imageinput = self.directoryfiles + imageinput
        self.cascPath = self.directorycurrent + "/configuration/haarcascade_frontalface_alt.xml"
        self.imageoutput = self.directoryfiles + imageoutput

    def detect(self):
        faceCascade = cv2.CascadeClassifier(self.cascPath)
        image = cv2.imread(self.imageinput)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        print "Found {0} faces!".format(len(faces))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imwrite(self.imageoutput, image)
        cv2.waitKey(0)

def recognizeFaces():

    idFaceRecognition = xFaceRecognition()
    idFaceRecognition.detect()

if __name__ == "__main__":

    idFaceRecognition = xFaceRecognition()
    idFaceRecognition.detect()
