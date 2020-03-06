import time
import pigpio
import random

MOTOR = 18  # Connect servomotor to BCM 18
DELAY = 2
pi = pigpio.pi()
if not pi.connected:
    exit(0)
pi.set_servo_pulsewidth(MOTOR, 0)

servoState = 'WAIT_FOR_BUTTON'


def move_to_angle(degrees):
    if (1000 <= degrees <= 2000):
        print('setting angle = ', degrees, ' degrees')
        pi.set_servo_pulsewidth(MOTOR, degrees)
    else:
        print('Invalid Angle')


def switchCallback(gpio, level, tick):
    global servoState
    servoState = 'RANDOM_MOVE'


pi.set_pull_up_down(12, pigpio.PUD_UP)
pi.set_glitch_filter(12, 200)
callBack = pi.callback(12, pigpio.FALLING_EDGE, switchCallback)

try:
    while True:
        if (servoState == 'RANDOM_MOVE'):
            move_to_angle(random.randint(1000, 2000))
            servoState = 'WAIT_FOR_BUTTON'
except KeyboardInterrupt:
    callBack.cancel()
    pi.stop()
