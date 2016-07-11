import wiringpi as pi, time

switch_mode_time = 15
blank_time = 10

led_pin = 23
sw_pin = 17

pi.wiringPiSetupGpio()
pi.pinMode( led_pin, 1 )

pi.pinMode( sw_pin, 0 )
pi.pullUpDnControl( sw_pin, 2)

last_time = 0
before_sw = 0
mode = 0
sw_mode = 1
led = 0
data = [ 1, blank_time ]
count = 0

while True:
	now_time = time.time()

	if ( mode == 0 ):
		if ( pi.digitalRead( sw_pin ) == 0 ):
			time.sleep( 0.01 )
			pi.digitalWrite( led_pin, 0 )
			mode = 1
			last_time = now_time
			count = 0
			sw_mode = 1

		elif ( sw_mode == 1 ):
			pi.digitalWrite( led_pin, 1 )
			led = 1
			sw_mode = 0
			last_time = now_time

		else:
			if ( count < len( data ) ):
				if ( now_time > last_time + data[count] ):
					if ( led == 0 ):
						pi.digitalWrite( led_pin, 1 )
						led = 1
					else:
						pi.digitalWrite( led_pin, 0 )
						led = 0
					last_time = now_time
					count = count + 1
			else:
				count = 0
				sw_mode = 1
	else:
		if ( now_time > last_time + switch_mode_time and before_sw == 1 ):
			sw_mode = 1
			mode = 0
			data.append( blank_time )

		else:
			if ( sw_mode == 1 ):
				last_time = now_time
				mode = 1
				sw_mode = 0
				before_sw = 0
				data = []

			if ( pi.digitalRead( sw_pin ) != before_sw ):
				time.sleep( 0.01 )
				data.append( now_time - last_time )
				last_time = now_time
				if ( before_sw == 1 ):
					before_sw = 0
				else:
					before_sw = 1



