# Log temperature every 10 seconds
import smbus
import sqlite3
import time
import sys
import signal
# constants
BUS = 1  # I2C bus number
ADDRESS = 0x48  # TC74 I2C bus address
FILENAME = 'temperature.db'
TABLE = 'TemperatureData'
PERIOD = 10.0


def sigint_handler(signum, frame):
    ''' SIGINT handler'''
    global db
    db.close()
    sys.exit(0)


def timer_handler(signum, frame):
    ''' Periodic timer signal handler'''
    global bus
    global db
    global cursor
    temp = bus.read_byte(ADDRESS)  # Read TC74 sensor
    # Insert data into database
    sqlcmd = "INSERT INTO " + TABLE + \
        " VALUES (datetime('now','localtime'),"+str(temp)+")"
    cursor.execute(sqlcmd)
    sqlcmd = "DELETE FROM " + TABLE + " WHERE datetime < datetime('now','localtime','-1 hour')"
    cursor.execute(sqlcmd)
    db.commit()


# Connect to I2C bus
bus = smbus.SMBus(BUS)
# Connect to the database
db = sqlite3.connect(FILENAME)
cursor = db.cursor()
# setup a sigint handler
signal.signal(signal.SIGINT, sigint_handler)
# Setup signal to call handler every PERIOD seconds
signal.signal(signal.SIGALRM, timer_handler)
signal.setitimer(signal.ITIMER_REAL, 1, PERIOD)
# Continuously loop blocking on signals
while True:
    signal.pause()  # block on signal, handler is called automatically
