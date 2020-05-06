#!/usr/bin/env python
# -*- coding: utf8 -*-

# This program is for a rasberry pi to interface with a connected RFID module (RC522) and detect what RFID chip
# is being connected to it.  If its unique identifier matches the saved one, then it lights up the green light and
# sends a message to grant access over the MQTT server.  If it is not the saved one, then it lights up the red led
# and sends a message to deny access.  It also logs the date/time and the unique id when a rfid is rejected.

# Imports
import RPi.GPIO as GPIO
import mfrc522
import signal
import time
import paho.mqtt.client as mqtt
import os
import datetime

# Constants/Globals
BROKER = 'iot.cs.calvin.edu'
USERNAME = "cs300"  # Put broker username here
PASSWORD = "safeIoT"  # Put broker password here
PORT = 8883
QOS = 0
DELAY = 5.0
TOPIC = 'QandT/FinalProj'
CERTS = '/etc/ssl/certs/ca-certificates.crt'
continue_reading = True
my_uid = [217, 164, 46, 195, 144]

# Capture SIGINT for cleanup when the script is aborted


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


# Callback when a connection has been established with the MQTT broker


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected to', BROKER)
    else:
        print('Connection to', BROKER, 'failed. Return code=', rc)
        os._exit(1)


client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set(USERNAME, password=PASSWORD)
client.tls_set(CERTS)
client.connect(BROKER, PORT, 60)
client.loop_start()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class mfrc522
MIFAREReader = mfrc522.MFRC522()

# Welcome message
print("Welcome to the mfrc522 data read example")
print("Press Ctrl-C to stop.")

# Configure LED Output Pin
LED1 = 36
GPIO.setup(LED1, GPIO.OUT)
GPIO.output(LED1, GPIO.LOW)

LED2 = 32
GPIO.setup(LED2, GPIO.OUT)
GPIO.output(LED2, GPIO.LOW)

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")

    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," +
              str(uid[2]) + "," + str(uid[3]) + ',' + str(uid[4]))

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Check to see if card UID read matches your card UID
        if uid == my_uid:
            print("Access Granted")
            GPIO.output(LED1, GPIO.HIGH)  # Turn on green LED
            client.publish(TOPIC,
                           'Access Granted')  # Publish that it was granted
            time.sleep(7)  # Wait 7 Seconds
            GPIO.output(LED1, GPIO.LOW)  # Turn off green LED

        else:
            GPIO.output(LED2, GPIO.HIGH)  # Turn on red LED
            client.publish(TOPIC, 'Access Denied')
            print("Access Denied!")  # Publish that it was denied
            file = open("Rejects.txt",
                        "r")  # Read in the rejects log and store it temp
            tempFile = file.read()
            file.close()
            file = open(
                "Rejects.txt",
                "w")  # Write back the rejects log and add an entry to it
            file.write(tempFile + "Bad card: " +
                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +
                       ": " + str(uid[0]) + "," + str(uid[1]) + "," +
                       str(uid[2]) + "," + str(uid[3]) + ',' + str(uid[4]) +
                       "\n")
            file.close()
            time.sleep(7)  # Wait 7 Seconds
            GPIO.output(LED2, GPIO.LOW)  # Turn off red LED
