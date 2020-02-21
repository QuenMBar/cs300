import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lightState = 0


def switchCallback(channel):
    global lightState
    if (lightState == 0):
        GPIO.output(16, True)
        lightState = 1
    else:
        GPIO.output(16, False)
        lightState = 0


GPIO.add_event_detect(12,
                      GPIO.FALLING,
                      callback=switchCallback,
                      bouncetime=300)

time.sleep(60)
