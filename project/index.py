import RPi.GPIO as io
io.setmode(io.BCM)
import time

#Motor 1
in1_pin = 22 
in2_pin = 27 
en1_2 = 18

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(en1_2, io.OUT)
#Motor 2
in3_pin = 17
in4_pin = 5
en3_4 = 15
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(en3_4, io.OUT)

duty = 50

pwm1_2=io.PWM(en1_2, 100)
pwm3_4=io.PWM(en3_4, 100)


pwm1_2.start(0)
pwm3_4.start(0)

def clockwise(in1, in2):
    io.output(in1, True)    
    io.output(in2, False)
    
    

def counter_clockwise(in1,in2):
    io.output(in1, False)
    io.output(in2, True)
    
pwm1_2.ChangeDutyCycle(duty)
pwm3_4.ChangeDutyCycle(duty)
try:
    while True :
        counter_clockwise(in1_pin,in2_pin)
        clockwise(in3_pin,in4_pin)
        print(".")   
except KeyboardInterrupt:
    pass
io.output(en1_2, False)
io.output(en3_4, False)
print("Stopped")
pwm1_2.stop()
pwm3_4.stop()
io.cleanup()
