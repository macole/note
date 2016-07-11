import wiringpi as pi, time
from mcp3002 import mcp3002

wait_time = 0.001
change_light = 500

col_line = 5
row_line = 7
anode_pin = [18, 22, 23, 24, 25]
cathod_pin = [12, 13, 19, 16, 26, 20, 21]

data_1 = [	0b00100,
			0b00100,
			0b11111,
			0b01110,
			0b01010,
			0b10001,
			0b00000 ]

data_2 = [	0b00111,
			0b10111,
			0b00011,
			0b01000,
			0b10010,
			0b00010,
			0b00000 ]

SPI_CH = 0
READ_CH = 0

mcp3002 = mcp3002( pi, SPI_CH )

pi.wiringPiSetupGpio()
for target in anode_pin:
	pi.pinMode( target, 1 )
	pi.digitalWrite( target, 0 )
for target in cathod_pin:
	pi.pinMode( target, 1 )
	pi.digitalWrite( target, 0 )

while True:
	value = mcp3002.read( pi, READ_CH )

	if ( value < change_light ):
		target_data = data_1
	else:
		target_data = data_2

	row = 0
	while row < row_line:
		col = 0
		logic_and = 0b10000
		while col < col_line:
			pi.digitalWrite( anode_pin[col], target_data[row] & logic_and )
			col = col + 1
			logic_and = logic_and >> 1

		pi.digitalWrite( cathod_pin[row], 1 )
		time.sleep( wait_time )
		pi.digitalWrite( cathod_pin[row], 0 )
		row = row + 1


