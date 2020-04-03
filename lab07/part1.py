# CS300 MQTT Lab
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
# Constants
BROKER = 'test.mosquitto.org' # Set the MQTT broker (change if needed)
PORT = 1883
QOS = 0
IN1 = 12
IN2 = 7
# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
# Use GPIO 12 as button inputs
GPIO.setup(IN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(IN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Setup MQTT client and callbacks
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Callback function when button is pressed
def button_callback1(channel):
    global client
    (result, num) = client.publish('Qmb2/button', 'Button pressed1', qos=QOS)
    if result != 0:
        print('PUBLISH returned error:', result)

def button_callback2(channel):
    global client
    (result, num) = client.publish('Qmb2/button', 'Button pressed2', qos=QOS)
    if result != 0:
        print('PUBLISH returned error:', result)

# Detect a falling edge on input pin
GPIO.add_event_detect(IN1, GPIO.FALLING, callback=button_callback1, bouncetime=500)
GPIO.add_event_detect(IN2, GPIO.FALLING, callback=button_callback2, bouncetime=500)
client.loop_start()
while True:
    time.sleep(10)
print("Done")
client.disconnect()
GPIO.cleanup() # clean up GPIO
