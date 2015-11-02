#!/usr/bin/python

import paho.mqtt.client as paho

class xMqttPub(object):

    def __init__(self):
        self.client = paho.Client()
        self.client.on_publish = self.on_publish
        self.client.connect("test.mosquitto.org", 1883, 60)

    def on_publish(self, mosq, obj, msg):
        print("Value set!")

    def write(self, value):
        self.client.publish("temp/random", value)

if __name__ == "__main__":

    xmqttpub = xMqttPub()
    xmqttpub.write("43")
