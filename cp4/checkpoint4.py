
# Import I/O expander chip library and time library
from DAH import PCF8574
import time
# Setup chip
pcf = PCF8574(address=0x38)
#Initialize Switch and Pattern Number
SWITCH0 = 7
patternNumber = 0 

def listen(i):
  """Listens to press button clicks and changes patternNumber to i if button is clicked.

  Args:
      i (int): Next pattern number
  """
  if (pcf.digitalRead(SWITCH0)):
      patternNumber = i
      print("Starting New Pattern, Ending Previous Pattern")
        
def loopPattern(r,i):
  """Takes in a list of LED ON states and loops over it. 

  Args:
      r (list): list of LED ON states
      i (int): Next pattern number
  """
  for state in r:
      listen(i)
      pcf.portWrite(state)
      # Replicates time.sleep but also listens to press button during the sleep.
      t = time.time() + 0.2
      while time.time() < t:
          listen(i)
      

while True:
  while patternNumber == 0:
      loopPattern([1, 2, 4, 8],1)   
  while patternNumber == 1:
      loopPattern([0, 15, 0, 15],0)
                
                
