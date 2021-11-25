import RPi.GPIO as io
io.setmode(io.BCM)
import time

#Motor 1
in1_pin = 23 
in2_pin = 24 
en1_2 = 18

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(en1_2, io.OUT)
#Motor 2
in3_pin = 27
in4_pin = 22
en3_4 = 17
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(en3_4, io.OUT)
#Avoidance 
io_pin = 2
isObst = True
io.setup(io_pin, io.IN)

duty = 70

pwm1_2=io.PWM(en1_2, 100)
pwm3_4=io.PWM(en3_4, 100)


pwm1_2.start(0)
pwm3_4.start(0)

deg90 = 0.7

def clockwise(in1, in2):
    io.output(in1, True) 
    io.output(in2, False)
def counter_clockwise(in1,in2):
    io.output(in1, False)
    io.output(in2, True)
def backward():
    clockwise(in1_pin,in2_pin)
    clockwise(in3_pin,in4_pin)
def forward():
    counter_clockwise(in1_pin,in2_pin)
    counter_clockwise(in3_pin,in4_pin)
def turn_right(start_time,degtime):
    
        end_time = start_time + degtime
        counter_clockwise(in1_pin,in2_pin)
        clockwise(in3_pin,in4_pin)
        
        if time.time() >= end_time:
            return False
        else:
            return True
def turn_left(start_time,degtime):
        end_time = start_time + degtime
        clockwise(in1_pin,in2_pin)
        counter_clockwise(in3_pin,in4_pin)
        
        if time.time() >= end_time:
            return False
        else:
            return True
pwm1_2.ChangeDutyCycle(duty)
pwm3_4.ChangeDutyCycle(duty)
try:
    while True :
        while (0 != io.input(io_pin)):
          forward()
        i = True
        start = time.time()
        while i ==True:
            i = turn_right(start,deg90)
            print(i)
        print(".")
except KeyboardInterrupt:
    pass
io.output(en1_2, False)
io.output(en3_4, False)
print("Stopped")
pwm1_2.stop()
pwm3_4.stop()
io.cleanup()
