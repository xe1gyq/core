#!/usr/bin/python

import ConfigParser
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time

class xPlotLy(object):

    def __init__(self, title):

        self.title = title
        self.configuration = ConfigParser.ConfigParser()
        self.configuration.read('configuration/credentials.config')
        self.username = self.configuration.get('plotly','username')
        self.apikey = self.configuration.get('plotly','apikey')
        self.streamtoken = self.configuration.get('plotly','streamtoken')

        py.sign_in(self.username, self.apikey)

    def setup(self):

        stream_temperature = Scatter(
            x=[],
            y=[],
            stream=dict(
                token=self.streamtoken,
            )
        )

        layout = Layout(
            title = self.title
        )

        this = Figure(data=[stream_temperature], layout=layout)
        py.plot(this, filename=self.title, auto_open=False)

        self.stream = py.Stream(self.streamtoken)
        self.stream.open()
        time.sleep(5)

    def graph(self, x, y):

        self.stream.write({'x': x, 'y': y})

if __name__ == "__main__":

    xpl = xPlotLy("Core PlotLy")
    xpl.setup()
    counter = 0
    while True:
        xpl.graph(counter, counter+1)
        counter += 1
        time.sleep(0.25)

# End of File
