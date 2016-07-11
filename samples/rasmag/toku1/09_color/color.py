import wiringpi as pi, time
from mcp3002 import mcp3002

green_pin = 18
blue_pin = 23
red_pin = 24
button_pin = 17

red = 0
blue = 0
green = 0
select = 0

SPI_CH = 0
READ_CH = 0

pi.wiringPiSetupGpio()
pi.pinMode( green_pin, 1 )
pi.pinMode( blue_pin, 1 )
pi.pinMode( red_pin, 1 )

pi.pinMode( button_pin, 0 )
pi.pullUpDnControl( button_pin, 2 )

pi.softPwmCreate( green_pin, 0, 100 )
pi.softPwmCreate( blue_pin, 0, 100 )
pi.softPwmCreate( red_pin, 0, 100 )

mcp3002 = mcp3002( pi, SPI_CH )

while True:
	if ( pi.digitalRead( button_pin ) == 0 ):
		time.sleep( 0.01 )
		if ( select == 0 ):
			select = 1
			print( "Control Green." )
		elif ( select == 1 ):
			select = 2
			print( "Control Blue." )
		elif ( select == 2 ):
			select = 0
			print( "Control Red." )
		while ( pi.digitalRead( button_pin ) == 0 ):
			time.sleep( 0.01 )

	val = mcp3002.read( pi, READ_CH )
	tmp_val = val / 1023

	if ( select == 0 ):
		red = tmp_val
	elif ( select == 1 ):
		green = tmp_val
	elif ( select == 2 ):
		blue = tmp_val

	pi.softPwmWrite( green_pin, int( green * 100 ) )
	pi.softPwmWrite( blue_pin, int( blue * 100 ) )
	pi.softPwmWrite( red_pin, int( red * 100 ) )

	time.sleep( 0.01 )

