import wiringpi as pi, time
import picamera

inv_time = 300
wait_time = 1

save_dir = "/home/pi/camera/"

hl_pin = 17

camera = picamera.PiCamera()
camera.resolution = ( 1920 , 1080 )

pi.wiringPiSetupGpio()
pi.pinMode( hl_pin, 0 )
pi.pullUpDnControl( hl_pin, 2)

cap_time = 0

while True:
	now_time = round( time.time() )
	if ( pi.digitalRead( hl_pin ) == 1 ):
		if ( now_time > cap_time + inv_time ):
			save_file = save_dir + time.strftime("%Y%m%d%H%M%S") + ".jpg"
			camera.capture( save_file )
			cap_time = now_time
			print ( "capture:", save_file )

	time.sleep( wait_time )
