

class hsv_rgb:
	def __init__( self, h, s, v ):
		self.h = float(h)
		self.s = float(s)
		self.v = float(v)
		self.r = 0.0
		self.g = 0.0
		self.b = 0.0
	
	def to_rgb( self ):
		if self.s == 0.0:
			return self.v, self.v, self.v
		i = int( self.h * 6.0 )
		f = ( self.h * 6.0 ) - float(i)
		p = self.v * ( 1.0 - self.s )
		q = self.v * ( 1.0 - self.s * f )
		t = self.v * ( 1.0 - self.s * ( 1.0 - f ) )
		i = i % 6
		if ( i == 0 ):
			self.r = self.v
			self.g = t
			self.b = p
		elif ( i == 1 ):
			self.r = q
			self.g = self.v
			self.b = p
		elif ( i == 2 ):
			self.r = p
			self.g = self.v
			self.b = t
		elif ( i == 3 ):
			self.r = p
			self.g = q
			self.b = self.v
		elif ( i == 4 ):
			self.r = t
			self.g = p
			self.b = self.v
		elif ( i == 5 ):
			self.r = self.v
			self.g = p
			self.b = q

	def set_hsv( self, h, s, v ):
		self.h = h
		self.s = s
		self.v = v
		self.to_rgb()

	def get_rgb( self ):
		return ( self.r, self.g, self.b )


