# This program turns on the light when the switch is pressed.
# It uses a call back function to do this.
#
# By Quentin Barnes
#

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# Set pin 16 to control the light and 12 for the switch
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lightState = 0


# Callback function that turns the light on or off
def switchCallback(channel):
    global lightState
    if (lightState == 0):
        GPIO.output(16, True)
        lightState = 1
    else:
        GPIO.output(16, False)
        lightState = 0


# Detects whenever the switch turns on, and calls the callback
GPIO.add_event_detect(12,
                      GPIO.FALLING,
                      callback=switchCallback,
                      bouncetime=300)

# How long the program will run for
time.sleep(60)
