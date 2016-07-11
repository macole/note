import wiringpi as pi, time, math
from lis3dh import lis3dh

sleep_time = 0.01

servo_pin = 18

pi.wiringPiSetupGpio()
pi.pinMode( servo_pin, 2 )
pi.pwmSetMode(0)
pi.pwmSetRange(1024)
pi.pwmSetClock(375)

SPI_CS = 0

lis3dh = lis3dh( pi, SPI_CS )

angle_deg = 0.0

while True:
	x= lis3dh.read( pi, "x" )
	y= lis3dh.read( pi, "y" )
	z= lis3dh.read( pi, "z" )

	angle_reg = math.atan2( y, z )
	angle_deg_new = math.degrees( angle_reg )

	angle_deg = angle_deg * 0.9 + angle_deg_new * 0.1

	print ("x:", x, "  y:", y, "  z:", z, " angle:", angle_deg)

	if ( angle_deg <= 90 and angle_deg >= -90 ):
		move_deg = int( 74 + 48 / 90 * angle_deg )
		pi.pwmWrite( servo_pin, move_deg )

	time.sleep( sleep_time )

