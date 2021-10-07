

# Import DAC chip library nd time
#from DAH import MCP4922
from DAH import MCP3208
import time
# pylab has a LOT of useful things in it.  Google for it.
import pylab
# numpy is the fundamental package for scientific computing with Python. Google for it.
import numpy as np



# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )
#Set MCP3208 Channel
channel = 0
time_list = []
voltage_list = []
high = []
low =[]
t0 =time.time()*1000
for i in range(100):
	
	t =  time.time()*1000-t0
	voltage = ADC0.analogReadVolt( channel )
	time_list.append(t)
#	if voltage > 0.75:
	#	high.append(voltage)
	#else:
	#	low.append(voltage)	
	voltage_list.append(voltage)



#average_high = np.mean(high)
#average_low = np.mean(low)
#print(average_high,average_low)

pylab.plot(time_list,voltage_list)
pylab.xlabel('Time (ms)')
pylab.ylabel('Voltage (V)')
pylab.title('Voltage v/s Time')
pylab.grid(True)
pylab.savefig("max.pdf")
pylab.show()
