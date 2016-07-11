import time, wiringpi as pi, os, struct

class adt7410:
	def __init__( self, wp, addr ):
		self.addr = addr
		self.i2c = wp.I2C()
		self.temp_dev = self.i2c.setup(self.addr)
		self.i2c.writeReg8(self.temp_dev,0x03, 0x80)
		
	def read_temp( self ):
		temp_data = struct.unpack('2B', os.read(self.temp_dev,2))
		temp = ( ( temp_data[0] << 8 ) + temp_data[1] )
		if ( temp_data[0] >= 0x80 ):
			temp = temp - 65536
		temp = temp / 128
		return ( temp )
