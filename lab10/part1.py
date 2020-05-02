# CS300 Periodic MQTT traffic generator
import paho.mqtt.client as mqtt
import time
import os
# Constants
BROKER = 'mqtt.eclipse.org'
PORT = 1883
QOS = 0
DELAY = 5.0
TOPIC = 'Qmb2/test'


# Callback when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to', BROKER)
    else:
        print('Connection to', BROKER, 'failed. Return code=', rc)
        os._exit(1)


# Setup MQTT client and callbacks
client = mqtt.Client()
client.on_connect = on_connect
# Connect to MQTT broker
client.connect(BROKER, PORT, 60)
client.loop_start()
# Continuously publish message
try:
    while True:
        print('Sending MQTT message')
        client.publish(TOPIC, 'hello world')
        time.sleep(DELAY)
except KeyboardInterrupt:
    print("Done")
    client.disconnect()
