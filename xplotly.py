#!/usr/bin/python

import ConfigParser
import os
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import random
import time

class xPlotLy(object):

    def __init__(self, title):
        self.title = title
        self.directorycurrent = os.path.dirname(os.path.realpath(__file__))
        self.directoryconfiguration = self.directorycurrent + '/../configuration/'
        self.configuration = ConfigParser.ConfigParser()
        self.credentialspath = self.directoryconfiguration + "credentials.config"
        self.configuration.read(self.credentialspath)
        self.username = self.configuration.get('plotly','username')
        self.apikey = self.configuration.get('plotly','apikey')
        self.streamtoken = self.configuration.get('plotly','streamtoken')

        py.sign_in(self.username, self.apikey)

        stream_data = Scatter(
            x=[],
            y=[],
            stream=dict(
                token=self.streamtoken,
            )
        )

        layout = Layout(
            title = self.title
        )

        this = Figure(data=[stream_data], layout=layout)
        py.plot(this, filename=self.title, auto_open=False)

        self.stream = py.Stream(self.streamtoken)
        self.stream.open()
        time.sleep(5)

    def graph(self, x, y):

        self.stream.write({'x': x, 'y': y})

if __name__ == "__main__":

    xPlotly = xPlotLy("Core PlotLy Random")
    counter = 0
    while True:
        xPlotly.graph(counter, random.random())
        counter += 1
        time.sleep(0.5)

# End of File
