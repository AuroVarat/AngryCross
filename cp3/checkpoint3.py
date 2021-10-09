from DAH import MCP3208
import time
import pylab
import numpy as np

# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )
#Set MCP3208 Channel
channel = 0


time_list = []
voltage_list = []

t0 =time.time()*1000 #Initial time in ms.q1	
for i in range(100):
	
	t =  time.time()*1000-t0
	voltage = ADC0.analogReadVolt( channel )
	time_list.append(t)
	voltage_list.append(voltage)
	

	
#Plotting Voltage changes against time
pylab.plot(time_list,voltage_list)
pylab.xlabel('Time (ms)')
pylab.ylabel('Voltage (V)')
pylab.title('Voltage v/s Time')
pylab.grid(True)
pylab.savefig("output.pdf")
pylab.show()
