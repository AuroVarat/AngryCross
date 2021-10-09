from DAH import MCP3208
import time
import pylab
import numpy as np

# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )
#Set MCP3208 Channel
channel = 0

#For analysing square-wave martrix
high_volt = []
low_volt =[]


for i in range(100):
	

	voltage = ADC0.analogReadVolt( channel )
  #0.75 because a voltage of 1.5 V was used for high voltage.
	if voltage > 0.75:
		high_volt.append(voltage)
	else:
		low_volt.append(voltage)
		
	


#calculating the high voltage end and low voltage end of a square wave.
average_high = np.mean(high)
average_low = np.mean(low)
print(average_high,average_low)
