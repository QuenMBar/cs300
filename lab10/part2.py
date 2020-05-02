# CS300 secure MQTT traffic generator
import paho.mqtt.client as mqtt
import time
import os
# Constants
BROKER = 'iot.cs.calvin.edu'
USERNAME = "cs300" # Put broker username here
PASSWORD = "safeIoT" # Put broker password here
PORT = 8883
QOS = 0
DELAY = 5.0
TOPIC = 'Qmb2/greeting'
CERTS = '/etc/ssl/certs/ca-certificates.crt'
# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print('Connected to',BROKER)
    else:
        print('Connection to',BROKER,'failed. Return code=',rc)
        os._exit(1)

# Setup MQTT client and callbacks
client = mqtt.Client()
client.on_connect = on_connect
# Securely connect to MQTT broker
client.username_pw_set(USERNAME, password=PASSWORD)
client.tls_set(CERTS)
client.connect(BROKER, PORT, 60)
client.loop_start()
# Continuously publish message
try:
    while True:
        print('publishing mqtt message')
        client.publish(TOPIC, 'hello world')
        time.sleep(DELAY)
except KeyboardInterrupt:
    print("Done")
    client.disconnect()
