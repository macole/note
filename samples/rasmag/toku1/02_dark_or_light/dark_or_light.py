import wiringpi as pi, time

led_pin = 23
cds_pin = 17

pi.wiringPiSetupGpio()
pi.pinMode( led_pin, 1 )
pi.pinMode( cds_pin, 0 )

while True:
    if ( pi.digitalRead(cds_pin) == 1 ):
        pi.digitalWrite( led_pin, 0 )
    else:
        pi.digitalWrite( led_pin, 1 )

