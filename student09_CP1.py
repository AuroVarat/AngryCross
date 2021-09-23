
# Import GPIO library
import RPi.GPIO as GPIO
import time
# Configure standard GPIO mode
# "BCM" refers to the Broadcom processor
GPIO.setmode(GPIO.BCM)
print("gekko")
# A variable to store the pin number for the LED
LED0 = 23

# Control the LED
  # Set pin as output
GPIO.setup(LED0, GPIO.OUT)

GPIO.output(LED0, GPIO.HIGH) # Turn on the LED

GPIO.output(LED0, GPIO.LOW)  # Turn off the LED
