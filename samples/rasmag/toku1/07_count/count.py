import wiringpi as pi, time

blank_time = 2
switch_time = 1

hl_pin = 17
disp_pin = 15
d0_pin = 18
d1_pin = 23
d2_pin = 24
d3_pin = 25

pi.wiringPiSetupGpio()
pi.pinMode( hl_pin, 0 )
pi.pullUpDnControl( hl_pin, 2)

pi.pinMode( disp_pin, 1 )
pi.pinMode( d0_pin, 1 )
pi.pinMode( d1_pin, 1 )
pi.pinMode( d2_pin, 1 )
pi.pinMode( d3_pin, 1 )

count = 0
pole = 0

while True:
	if ( pi.digitalRead( hl_pin ) == 1 ):
		if ( pole == 0 ):
			count = count + 1
			pole = 1
	else:
		if ( pole == 1 ):
			pole = 0

	disp = str( count )

	i = 0

	pi.digitalWrite( disp_pin, 1 )
	while (  i < len(disp) ):
		pi.digitalWrite( d0_pin, int(disp[i]) & 0x01 )
		pi.digitalWrite( d1_pin, int(disp[i]) & 0x02 )
		pi.digitalWrite( d2_pin, int(disp[i]) & 0x04 )
		pi.digitalWrite( d3_pin, int(disp[i]) & 0x08 )
		i = i + 1
		time.sleep( switch_time )

	pi.digitalWrite( disp_pin, 0 )
	time.sleep( blank_time )

