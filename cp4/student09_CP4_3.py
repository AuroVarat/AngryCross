
# Import I/O expander chip library
from DAH import PCF8574
import time
# Setup chip
pcf = PCF8574(address=0x38)

def firstPattern():
    """
    Three on at a time
    """
    return [1, 2, 4, 8]
   
    
def secondPattern():
    return [15, 0, 15, 0]
    

SWITCH0 = 7
value = True

while True:
   
        r = firstPattern()
      
        for i in r:
            if (pcf.digitalRead(SWITCH0)):
                if value:
                    r = secondPattern()
                else:
                    r = firstPattern()
              
            pcf.portWrite(i)
            time.sleep(0.2)
            
 
