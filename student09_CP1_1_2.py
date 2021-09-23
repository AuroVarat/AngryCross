
# Import GPIO library
import RPi.GPIO as GPIO
import time
# Configure standard GPIO mode
# "BCM" refers to the Broadcom processor
GPIO.setmode(GPIO.BCM)

# A variable to store the pin number for the LED
LED0 = 23

# Control the LED
GPIO.setup(LED0, GPIO.OUT)   # Set pin as output




while True: # Loop forever (effectively "while True equals True")

    value = not GPIO.input(LED0) # Store inverted LED value
    GPIO.output(LED0, value)     # Use inverted value
    time.sleep(1)                # Wait 2 seconds
