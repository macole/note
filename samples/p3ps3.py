import sys
import serial
import os
import time
import datetime
file = open('/dev/input/js0','rb')
data = []
com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
LLR = 20		#Left analog stick Left - Right
LUD = 120		#Left analog stick UP - DOWN 
RLR = 100		#Right analog stick Left - Right
RUD = 0			#Right analog stick UP - DOWN

mode = "wait"
before_time = 0
now_time = 0

def comWrite(n):
	com.write(bytes(n, encoding='ascii'))

while 1:
	for character in file.read(1):
		data += ['%02X' % character]
#		data += ['%02X' % ord(character)]
		if len(data) == 8:
			if data[6] == '01':
				mode = "button" 
				if data[4] == '01': #pressed button
					if data[7] == '00': # SELECT
						sys.stdout.write('You pressed the SELECT button\n')
						
						
					elif data[7] == '01': #L3
						sys.stdout.write('You pressed the L3 button\n')
						

					elif data[7] == '02': #R3
						sys.stdout.write('You pressed the R3 button\n')
						
					
					elif data[7] == '03': #START
						sys.stdout.write('You pressed the START button\n')
						
					
					elif data[7] == '04': #UP	
						sys.stdout.write('You pressed the UP button\n')
						comWrite("#M1")
					
					elif data[7] == '05': #RIGHT
						sys.stdout.write('You pressed the RIGHT button\n')
						comWrite("#M3")
					
					elif data[7] == '06': #DOWN	
						sys.stdout.write('You pressed the DOWN button\n')
						comWrite("#M2")
					
					elif data[7] == '07': #LEFT	
						sys.stdout.write('You pressed the LEFT button\n')
						comWrite("#M4")
					
					elif data[7] == '08': #L2	
						sys.stdout.write('You pressed the L2 button\n')
						time.sleep(0.11)
						comWrite("#PS07A040T001")
					
					elif data[7] == '09': #R2	
						sys.stdout.write('You pressed the R2 button\n')
						time.sleep(0.11)
						comWrite("#PS04A080T001")
					
					elif data[7] == '0A': #L1	
						sys.stdout.write('You pressed the L1 button\n')
						time.sleep(0.11)
						comWrite("#PS07A080T001")
					
					elif data[7] == '0B': #R1
						sys.stdout.write('You pressed the R1 button\n')
						time.sleep(0.11)
						comWrite("#PS04A040T001")
					
					elif data[7] == '0C': #TRIANGLE	
						sys.stdout.write('You pressed the TRIANGLE button\n')
						comWrite("#M5")
					
					elif data[7] == '0D': #CIRCLE	
						sys.stdout.write('You pressed the CIRCLE button\n')
						comWrite("#M6")
					
					elif data[7] == '0E': #CROSS	
						sys.stdout.write('You pressed the CROSS button\n')
						comWrite("#M7")
					
					elif data[7] == '0F': #SQUARE	
						sys.stdout.write('You pressed the SQUARE button\n')
						comWrite("#M8")
					

				elif data[4] == '00': #released button
					
					if data[7] == '00': # SELECT
						sys.stdout.write('You released the SELECT button\n')
					elif data[7] == '01': #L3
						sys.stdout.write('You released the L3 button\n')
					elif data[7] == '02': #R3
						sys.stdout.write('You released the R3 button\n')
					elif data[7] == '03': #START
						sys.stdout.write('You released the START button\n')
					elif data[7] == '04': #UP	
						comWrite("#M0")
						sys.stdout.write('You released the UP button\n')
					elif data[7] == '05': #RIGHT
						comWrite("#M0")
						sys.stdout.write('You released the RIGHT button\n')	
					elif data[7] == '06': #DOWN
						comWrite("#M0")	
						sys.stdout.write('You released the DOWN button\n')
					elif data[7] == '07': #LEFT
						comWrite("#M0")	
						sys.stdout.write('You released the LEFT button\n')
					elif data[7] == '08': #L2
						time.sleep(0.11)
						comWrite("#PS07A060T001")	
						sys.stdout.write('You released the L2 button\n')
					elif data[7] == '09': #R2	
						time.sleep(0.11)
						comWrite("#PS04A060T001")
						sys.stdout.write('You released the R2 button\n')
					elif data[7] == '0A': #L1
						time.sleep(0.11)
						comWrite("#PS07A060T001")	
						sys.stdout.write('You released the L1 button\n')
					elif data[7] == '0B': #R1
						time.sleep(0.11)
						comWrite("#PS04A060T001")
						sys.stdout.write('You released the R1 button\n')
					elif data[7] == '0C': #TRIANGLE
						comWrite("#M0")	
						sys.stdout.write('You released the TRIANGLE button\n')
					elif data[7] == '0D': #CIRCLE
						comWrite("#M0")	
						sys.stdout.write('You released the CIRCLE button\n')
					elif data[7] == '0E': #CROSS
						comWrite("#M0")	
						sys.stdout.write('You released the CROSS button\n')
					elif data[7] == '0F': #SQUARE
						comWrite("#M0")	
						sys.stdout.write('You released the SQUARE button\n')
			elif data[6] == '02':
				
				now = datetime.datetime.now()
				now_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
				a_data = int(data[5],16)
				if a_data >= 0 and a_data < 128:
					a_data = a_data + 128
				elif a_data >= 128 and a_data < 256:
					a_data = a_data - 128


				if data[7] == '00':	#Left stick L-R		PS06
					a_data = (int(a_data/2.13) - 120) * -1
					a_data =int(( a_data - 60) * 1.66 + 20)
					if a_data <= 20:
						a_data = 20
					LLR = a_data
					joy = True
					mode = "analog"
							
				elif data[7] == '01':	#Left stick U-D		PS05
					a_data = int(a_data/2.13)
					a_data = a_data * 2
					if a_data >= 120:
						a_data = 120
					LUD = a_data
					joy = True
					mode = "analog"
					
				elif data[7] == '02':	#Right stick L-R	PS03
					a_data = (int(a_data/2.13) - 120) * -1
					a_data = int(a_data * 1.66)
					if a_data >= 100:
						a_data = 100
					RLR = a_data
					joy = True
					mode = "analog"
					
				elif data[7] == '03':	#Right stick U-D	PS02
					a_data = (int(a_data/2.13) - 120) * -1
					a_data = (a_data - 60 ) * 2
					if a_data <= 0:
						a_data = 0
					RUD = a_data
					joy = True
					mode = "analog"
					
				else:
					joy = False
				dif = now_time - before_time
				if dif > 110 and joy == True:
					comWrite("#PS02A" + str(RUD).zfill(3) + "S03A" + str(RLR).zfill(3) + "S05A" + str(LUD).zfill(3) + "S06A" + str(LLR).zfill(3) + "T001\r\n")
					
					comWrite("ms : " + str(dif) + "\r\n")
					now = datetime.datetime.now()
					before_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
			sys.stdout.flush()
			data = []			
	now = datetime.datetime.now()
	j_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
	dif = j_time - before_time
	if dif > 200 and mode == "analog":
		comWrite("#PS02A" + str(RUD).zfill(3) + "S03A" + str(RLR).zfill(3) + "S05A" + str(LUD).zfill(3) + "S06A" + str(LLR).zfill(3) + "T001\r\n")
		now = datetime.datetime.now()
		before_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
sys.stdout.flush()
data = []        
