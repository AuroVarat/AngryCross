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
#For analysing square-wave martrix
high_volt = []
low_volt =[]

t0 =time.time()*1000 #Initial time in ms.q1	
for i in range(100):
	
	t =  time.time()*1000-t0
	voltage = ADC0.analogReadVolt( channel )
	time_list.append(t)
	voltage_list.append(voltage)
	
	#Uncomment for recording square wave 
	if voltage > 0.75:
		high_volt.append(voltage)
	else:
		low_volt.append(voltage)
		
	


#calculating the high voltage end and low voltage end of a square wave.
average_high = np.mean(high)
average_low = np.mean(low)
print(average_high,average_low)
#Plotting Voltage changes against time
pylab.plot(time_list,voltage_list)
pylab.xlabel('Time (ms)')
pylab.ylabel('Voltage (V)')
pylab.title('Voltage v/s Time')
pylab.grid(True)
pylab.savefig("output.pdf")
pylab.show()
