import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
count = 0
state = 1  # Keeps track of the last state of the input
while True:
    if GPIO.input(12) == False and state == 1:
        count += 1
        print(count)
        state = 0
    if GPIO.input(12) == True and state == 0:
        state = 1
