import RPi.GPIO as io
io.setmode(io.BCM)
import time

in1_pin = 4
in2_pin = 17
en = 18
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(en, io.OUT)

pwm=io.PWM(en, 7000)
pwm.start(0)

def clockwise():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)

def counter_clockwise():
    io.output(in1_pin, False)
    io.output(in2_pin, True)



while True :
  

    counter_clockwise()
    pwm.ChangeDutyCycle(100)
    print("d")   
    
    
    
io.cleanup()
