"""DAH Robot Motion with Avoidance Sensor
By Auro Varat Patnaik & Luisa Schrempf 
Version 11/11/21
"""
import RPi.GPIO as io
io.setmode(io.BCM)
import time
from motionClass import motorControl as mc

#Avoidance 

io_pin = 2
isObst = True
io.setup(io_pin, io.IN)

#Motor 1
mc1 = mc.new_motor("Motor Left",23,24,18,100,True)
#Motor 2
mc2 = mc.new_motor("Motor Right",27,22,17,100,True)
#Speed
power = 50#%
wait= 0.7
motor_list = [mc1,mc2]



try:
    while True :
        while (0 != io.input(io_pin)):
            mc.forward(motor_list)
        z = True
        start = time.time()
        while z==True:
            z = mc.turn_right(motor_list,start,wait)
            print(z)
       
except KeyboardInterrupt:
    pass

mc1.stop()
mc2.stop()
