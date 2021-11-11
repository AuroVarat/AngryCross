import RPi.GPIO as io
import time
io.setmode(io.BCM)
io_pin = 2
isObst = True

io.setup(io_pin, io.IN)

try:
	while True:
		if (0 == io.input(io_pin)):
			print(" DETECTED: There is an obstacle ahead {}".format(time.time()))
		
except KeyboardInterrupt:
    pass
    
io.cleanup()
