# Import GPIO library
import RPi.GPIO as GPIO
import time
# Configure standard GPIO mode
# "BCM" refers to the Broadcom processor
GPIO.setmode(GPIO.BCM)

# A variable to store the pin number for the LED, Switch
SWITCH0 = 23
LED0 = 24

# Control the LED
GPIO.setup(SWITCH0, GPIO.IN)   # Set pin as input
GPIO.setup(LED0, GPIO.OUT)   # Set pin as OUTPUT

# Read the switch and if it is pressed toggle the state of the LED
while True:
    if (GPIO.input(SWITCH0) == GPIO.HIGH):
	value = not GPIO.input(LED0) # Store inverted LED value
	GPIO.output(LED0,value ) # Turn on the LED
	time.sleep(0.5)
   
	# Insert your code here
