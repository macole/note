import wiringpi as pi, time
from mcp3002 import mcp3002
from hsv_rgb import *

green_pin = 18
blue_pin = 23
red_pin = 24

saturation = 1.0
value = 1.0
vol_hue = 1.0

SPI_CH = 0
READ_CH = 0

hsv = hsv_rgb( vol_hue, saturation, value )

pi.wiringPiSetupGpio()
pi.pinMode( green_pin, 1 )
pi.pinMode( blue_pin, 1 )
pi.pinMode( red_pin, 1 )

pi.softPwmCreate( green_pin, 0, 100 )
pi.softPwmCreate( blue_pin, 0, 100 )
pi.softPwmCreate( red_pin, 0, 100 )

mcp3002 = mcp3002( pi, SPI_CH )

while True:
	val = mcp3002.read( pi, READ_CH )
	tmp_hue = val / 1023    
	vol_hue = vol_hue * 0.9 + tmp_hue * 0.1

	hsv.set_hsv( vol_hue, saturation, value )
	( red, green, blue ) = hsv.get_rgb()

	pi.softPwmWrite( green_pin, int( green * 100 ) )
	pi.softPwmWrite( blue_pin, int( blue * 100 ) )
	pi.softPwmWrite( red_pin, int( red * 100 ) )

	time.sleep( 0.01 )

