#!/usr/bin/python

import ConfigParser
import logging
import os
import re
import wolframalpha

class xWolfram(object):

    def __init__(self):
        self.directorycurrent = os.path.dirname(os.path.realpath(__file__))
        self.directoryconfiguration = self.directorycurrent + '/configuration/'
        self.configuration = ConfigParser.ConfigParser()
        self.credentialspath = self.directoryconfiguration + "credentials.config"
        self.configuration.read(self.credentialspath)
        appid=self.configuration.get("wolframalpha", "appid")
        self.client = wolframalpha.Client(appid)

    def question(self, question):
        try:
            res = self.client.query(question)
            string = re.sub('[^0-9a-zA-Z]+', ' ', next(res.results).text)
            return string
        except StopIteration:
            return 'There was no response!'

def askWolfram(question):
    idWolfram = xWolfram()
    answer = idWolfram.question(question)
    return answer

if __name__ == "__main__":

    idWolfram = xWolfram()
    print idWolfram.question("What is the capital of Mexico")

# End of File
