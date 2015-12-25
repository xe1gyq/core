#!/usr/bin/python

import paho.mqtt.client as paho

class xMqttPub(object):

    def __init__(self, server="test.mosquitto.org", port=1883):
        self.server = server
        self.port = port
        self.client = paho.Client()
        self.client.on_publish = self.on_publish
        self.client.connect(self.server, self.port, 60)

    def on_publish(self, mosq, obj, msg):
        print("xMqttPub Value Published!")

    def write(self, topic, value):
        self.client.publish(topic, value)

if __name__ == "__main__":

    xmqttpub = xMqttPub(server="test.mosquitto.org", port=1883)
    xmqttpub.write("temp/random", "43")
