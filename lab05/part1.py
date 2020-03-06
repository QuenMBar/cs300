import RPi.GPIO as GPIO
import time
# Constants
LED = 16 # LED connected to BCM 16
PWM_FREQ = 500 # frequency=500HZ
GPIO.setmode(GPIO.BCM) # Use BCM numbers
GPIO.setup(LED, GPIO.OUT) # Set LED to output mode.
pwm = GPIO.PWM(LED, PWM_FREQ) # Initialize PWM frequency
duty_cycle = 0
pwm.start(duty_cycle) # PWM with 0% duty cycle
while duty_cycle >= 0 and duty_cycle <=100:
    duty_cycle = int(input('Enter a PWM duty cycle (enter -1 to end): '))
    if duty_cycle == -1:
        break
    pwm.ChangeDutyCycle(duty_cycle)
    print("Duty cycle=",duty_cycle,'%')
pwm.stop()
GPIO.cleanup() # reset GPIO ports
