import RPi.GPIO as GPIO  # Import the GPIO library.
import time  # Import time library
# Constants
MOTOR = 18  # Connect servomotor to BCM 18
PWM_FREQ = 50  # Set PWM frequency to 50Hz
GPIO.setmode(GPIO.BCM)  # Use BCM numbers
GPIO.setup(MOTOR, GPIO.OUT)  # Set MOTOR pin to output mode.
pwm = GPIO.PWM(MOTOR, PWM_FREQ)
print('setting angle = 0 degrees')
pwm.start(7.5)
time.sleep(5)
print('setting angle = 90 degrees')
pwm.ChangeDutyCycle(10)
time.sleep(5)
print('setting angle = -90 degrees')
pwm.ChangeDutyCycle(5)
time.sleep(5)
pwm.stop()
GPIO.cleanup()
