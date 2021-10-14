
# Import I/O expander chip library
from DAH import PCF8574
import time
# Setup chip
pcf = PCF8574(address=0x38)

# A variable to store the pin number for the LED
LED0 = 0

# Turn off the LED by setting the pin high
pcf.digitalWrite(LED0, True)


while True: # Loop forever (effectively "while True equals True")

    value = not pcf.digitalRead(LED0) # Store inverted LED value
    pcf.digitalWrite(LED0, value)    # Use inverted value
    time.sleep(1)                # Wait 2 seconds
