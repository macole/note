import wiringpi as pi, time
from mcp3002 import mcp3002

alert = 10
buzzer_pin = 23

SPI_CH = 0
READ_CH = 0

pi.wiringPiSetupGpio()
pi.pinMode( buzzer_pin, 1 )

pi.digitalWrite( buzzer_pin, 0 )

mcp3002 = mcp3002( pi, SPI_CH )

def gp2y0a21( volt ):
    if ( volt >= 2.25 ):
        length = (volt - 4.625) / -0.2375
    elif ( volt < 2.25 and volt >= 1.7 ):
        length = (volt - 3.35) / -0.11
    elif ( volt < 1.7 and volt >= 1.3 ):
        length = (volt - 2.9) / -0.08
    elif ( volt < 1.3 and volt >= 0.9 ):
        length = (volt - 2.1) / -0.04
    elif ( volt < 0.9 and volt >= 0.6 ):
        length = (volt - 1.35) / -0.015
    elif ( volt < 0.6 and volt >= 0.5 ):
        length = (volt - 1.1) / -0.01
    elif ( volt < 0.5 ):
        length = (volt - 0.8) / -0.005
    return ( length )

while True:
    value = mcp3002.read( pi, READ_CH )

    volt = value * 3.3 / 1023    
    distance = gp2y0a21( volt )
    
    print ("Distance :" , distance , "cm")

    if ( distance < alert ):
        pi.digitalWrite( buzzer_pin, 1 )
    else:
        pi.digitalWrite( buzzer_pin, 0 )

    time.sleep( 0.1 )
