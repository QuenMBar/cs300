import time
import pigpio
# Constants
MOTOR = 18  # Connect servomotor to BCM 18
DELAY = 2
pi = pigpio.pi()
if not pi.connected:
    exit(0)
pi.set_servo_pulsewidth(MOTOR, 0)
try:
    while True:
        print('setting angle = -90 degrees')
        pi.set_servo_pulsewidth(MOTOR, 1000)
        time.sleep(DELAY)
        print('setting angle = 0 degrees')
        pi.set_servo_pulsewidth(MOTOR, 1500)
        time.sleep(DELAY)
        print('setting angle = 90 degrees')
        pi.set_servo_pulsewidth(MOTOR, 2000)
        time.sleep(DELAY)
except KeyboardInterrupt:
    pi.stop()
