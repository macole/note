import wiringpi as pi, time

class lis3dh:
	def __init__(self, wp, cs):
		self.cs = cs
		wp.wiringPiSPISetup( self.cs, 1000000 )
		
		buffer = 0x20 << 8 | 0x77
		buffer = buffer.to_bytes( 2, byteorder='big' )
		wp.wiringPiSPIDataRW( self.cs , buffer )

	def spi_read( self, wp, read_addr ):
		command = read_addr | 0x80
		buffer = command << 8
		buffer = buffer.to_bytes( 2, byteorder='big' )
		wp.wiringPiSPIDataRW( self.cs, buffer )
		return( buffer[1] )

	def conv_two_byte( self, high, low ):
		dat = high << 8 | low
		if ( high >= 0x80 ):
			dat = dat - 65536
		dat = dat >> 4
		return ( dat )

	def read(self, wp, axis ):
		if ( axis == "x" ):
			lb = self.spi_read( wp, 0x28 )
			hb = self.spi_read( wp, 0x29 )
			value = self.conv_two_byte( hb, lb )
		elif ( axis == "y" ):
			lb = self.spi_read( wp, 0x2a )
			hb = self.spi_read( wp, 0x2b )
			value = self.conv_two_byte( hb, lb )
		elif ( axis == "z" ):
			lb = self.spi_read( wp, 0x2c )
			hb = self.spi_read( wp, 0x2d )
			value = self.conv_two_byte( hb, lb )
		
		return value
