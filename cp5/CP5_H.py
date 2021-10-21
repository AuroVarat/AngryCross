from DAH import DS18B20
import pylab
import matplotlib.animation as animation
import time
import numpy as np

# Readout temperature sensor
tmp0 = DS18B20( address="10-00080379b4fb" )
tmp1 = DS18B20( address="10-0008037a6ba5" )

# Empty arrays of time and measurement values to plot
timeValues = [ ]
measurements0 = [ ]
measurements1 = [ ]

t0= time.time()
def updatePlot():
    t = time.time() - t0
    timeValues.append(t) # Store time
    measurements0.append( tmp0.getCelsius())           # Store temperature
    measurements1.append( tmp1.getCelsius())           # Store temperature
  
    return t
    
t = time.time() - t0
while t < 300:
    t = updatePlot()
    print(t)
    

pylab.title("Two Temperature Sensors at Ambient Temperature")
pylab.hist((measurements0,measurements1), bins=5, range=[22.75,23.0625],label=("Sensor 0","Sensor 1"),color=("darkseagreen","violet") )
pylab.xlabel("Temperature Bins (°C)")
pylab.ylabel("Counts")
pylab.legend()
pylab.show()

np.savetxt("output_temp.txt",np.c_[timeValues,measurements0,measurements1],delimiter=",",header="Time, S0, S1")
