import wiringpi as pi, time

class mcp3002:
	def __init__(self, wp, sc):
		self.sc = sc
		wp.wiringPiSPISetup( self.sc, 1000000 )

	def read(self, wp, ch):
		buffer = 0x6800 | (0x1800 * ch )
		buffer = buffer.to_bytes( 2, byteorder='big' )

		wp.wiringPiSPIDataRW( self.sc , buffer )
		value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff

		return value
