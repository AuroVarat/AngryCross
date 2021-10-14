
# Import I/O expander chip library
from DAH import PCF8574
import time
# Setup chip
pcf = PCF8574(address=0x38)

def firstPattern():
    """
    three on at a time
    """
    r = [1, 2, 4, 8]
    for i in r:
        pcf.portWrite(i)
        time.sleep(0.2)

    
def secondPattern():
    r = [0, 15, 0, 15]
    for i in r:
        pcf.portWrite(i)
        time.sleep(0.2)

SWITCH0 = 7

value = 0

while True:

        while value == 0:
            firstPattern() 
            if (pcf.digitalRead(SWITCH0)):
                value = 1
                print(value)
                
        while value == 1:
            secondPattern() 
            if (pcf.digitalRead(SWITCH0)):
                value = 0
                print(value)
                
                
