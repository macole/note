import wiringpi as pi, time
from mcp3002 import mcp3002

on_temp = 26
fan_pin = 23

SPI_CH = 0
READ_CH = 0

pi.wiringPiSetupGpio()
pi.pinMode( fan_pin, 1 )

pi.digitalWrite( fan_pin, 0 )

mcp3002 = mcp3002( pi, SPI_CH )

while True:
    value = mcp3002.read( pi, READ_CH )
    volt = value * 3.3 / 1023
    temp = volt * 100

    print (temp)

    if ( temp > on_temp ):
        pi.digitalWrite( fan_pin, 1 )
    else:
        pi.digitalWrite( fan_pin, 0 )



