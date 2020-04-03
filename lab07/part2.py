# CS300 MQTT Lab
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
# Constants
BROKER = 'test.mosquitto.org'
PORT = 1883
QOS = 0
LED1 = 16
LED2 = 20
# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
# Configure GPIO for LED output
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
# Callback when a connection has been established with the MQTT broker
def on_connect(client, userdata, rc, *extra_params):
    print('Connected with result code='+str(rc))
# Callback when client receives a message from the broker
# Use button message to turn LED on/off
def on_message(client, data, msg):
    if msg.topic == "Qmb2/button":
        if str(msg.payload) == "b'Button pressed1'":
            if GPIO.input(LED1) == 1:
                GPIO.output(LED1, 0)
            else:
                GPIO.output(LED1, 1)
        if str(msg.payload) == "b'Button pressed2'":
            if GPIO.input(LED2) == 1:
                GPIO.output(LED2, 0)
            else:
                GPIO.output(LED2, 1)
# Setup MQTT client and callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Connect to MQTT broker and subscribe to the button topic
client.connect(BROKER, PORT, 60)
client.subscribe("Qmb2/button", qos=QOS)
client.loop_start()
client.loop_start()
while True:
    time.sleep(10)
print("Done")
client.disconnect()
GPIO.cleanup() # clean up GPIO
