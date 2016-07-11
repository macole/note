import wiringpi as pi, time

inv_time = 1

led1_pin = 23
led2_pin = 24
sw_pin = 17

pi.wiringPiSetupGpio()
pi.pinMode( led1_pin, 1 )
pi.pinMode( led2_pin, 1 )
pi.pinMode( sw_pin, 0 )

light = 0

while ( True ):
	pi.digitalWrite( led1_pin, 0 )
	pi.digitalWrite( led2_pin, 0 )

	while ( pi.digitalRead(sw_pin) == 1 ):
		if ( light == 0 ):
			pi.digitalWrite( led1_pin, 1 )
			pi.digitalWrite( led2_pin, 0 )
			light = 1
		else:
			pi.digitalWrite( led1_pin, 0 )
			pi.digitalWrite( led2_pin, 1 )
			light = 0
		time.sleep( inv_time )

