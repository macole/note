import wiringpi as pi, time, os, struct
from sc1602 import sc1602
from adt7410 import adt7410

RS = 23
E  = 24
D4 = 22
D5 = 27
D6 = 17
D7 = 4

adt7410_addr = 0x48
temp = 0.0

adt7410 = adt7410( pi, adt7410_addr )

pi.wiringPiSetupGpio()
lcd = sc1602( RS, E, D4, D5, D6, D7 )

lcd.move_home( )
lcd.set_cursol( 0 )
lcd.set_blink( 0 )

while True:
	lcd.move( 0x00, 0x00 )
	lcd.write( time.strftime("%Y/%m/%d %H:%M", time.localtime()) )

	temp = adt7410.read_temp()

	out_char = "Temp: " + str( round( temp, 2 ) ) + " C  "
	lcd.move( 0x00, 0x01 )
	lcd.write( out_char )

	time.sleep(1)


