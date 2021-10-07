"""
Title: Checkpoint 2 
Description: Changing LED brightness using DAC. Exposing LDR to the LED's light and 
measuring the voltage output through ADC connected to the LDR with a potential divider.
Author: Auro Varat Patnaik and Luisa Schrempf
Version: 06/10/2021
"""
# Import ADC, DAC chip library and time
from DAH import MCP4922
from DAH import MCP3208
import time

# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )
#Set MCP3208 Channel
channel = 0 
# Define DAC as SPI chip 1 (CE1/GPIO7)
DAC1 = MCP4922( chip=1 )
# Output range of voltage on channel 0 of DAC1
volt_range = [0.5,1.8,2.0,2.5,2.8,3.0,3.3]
# Create and save a file containing voltage changes
file = open("output.txt","w")
file.write("#DAC Output Voltage tp LED,ADC Input Voltage from LDR\n")
for volt in volt_range:
	#Set Voltage output from DAC to LED
	DAC1.analogWriteVolt( 0, volt)
	#Print voltage from DAC and ADC
	print("Voltage at Channel 0 with Input "+str(volt)+ "V: "+ str(ADC0.analogReadVolt( channel )))
	#Write to file 
	file.write(str(volt)+","+str(ADC0.analogReadVolt( channel ))+"\n")
	#Set a sensible refresh rate 
	time.sleep(0.5)
#Turn off DAC output to turn off LED
DAC1.analogWriteVolt( 0, 0.0)
file.close()
