import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
for count in range(20):
    GPIO.output(16, True)
    time.sleep(0.5)
    GPIO.output(16, False)
    time.sleep(0.5)
print("Done!")
GPIO.cleanup()
