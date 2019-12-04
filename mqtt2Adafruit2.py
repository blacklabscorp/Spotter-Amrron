#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import datetime
import time
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO key and username
ADAFRUIT_IO_KEY      = 'f423599b45c04d2db94fece204600399'
ADAFRUIT_IO_USERNAME = 'romeo07'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("amrron/#")

def on_message(client, userdata, msg):
    print(str(datetime.datetime.now()) + ": " + msg.topic + " " + str(msg.payload))
    # Send the data to Adafruit IO. Replace topic with a feed name
    feedname=msg.topic.replace("/","_")
    print("Publish to Adafruit feedname: " + feedname)
    adafruitClient.publish(feedname,msg.payload)

# Initialize the client that should connect to the Mosquitto broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.190", 1883, 60)

# Initialize the client that should connect to io.adafruit.com
adafruitClient = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
adafruitClient.connect()
# Run loop in a separate thread
adafruitClient.loop_background()

# Blocking loop to the Mosquitto broker
client.loop_forever()
