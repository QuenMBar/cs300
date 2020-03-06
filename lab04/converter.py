# Program to continuously read A/D converter
from time import sleep
import Adafruit_MCP3008
# Software SPI pin configuration
CLK = 25
MISO = 24
MOSI = 23
CS = 18
# Instantiate a new A/D object
a2d = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
print('Press Ctrl-C to quit...')
while True:
    value = a2d.read_adc(0)
    print('A/D input channel 0 = ', value)
    sleep(0.1)
