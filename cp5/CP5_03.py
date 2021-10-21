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

# Set up the plot object
plotFigure = pylab.figure()

# The function to call each time the plot is updated
t0 = time.time()
def updatePlot( i ):
  
    timeValues.append( time.time() -t0) # Store time
    measurements0.append( tmp0.getCelsius())           # Store temperature
    measurements1.append( tmp1.getCelsius())           # Store temperature
    plotFigure.clear()# Clear the old plot
    pylab.plot( timeValues, measurements0,label="Sensor 0",color="darkseagreen" ) # Make the new plot
    pylab.plot( timeValues, measurements1,label="Sensor 1" ,color="violet") # Make the new plot
    pylab.title("Temperature Variation as a Function of Time")   
    pylab.xlabel("Time (s)")
    pylab.ylabel("Temperature (°C)")
    pylab.legend()
# Make the animated plot

	
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=1000,frames=50 )
pylab.show()


print("Sensor 0 stats")
print("Mean: {} °C".format(np.mean(measurements0)))
print("Standard Deviation: {} °C".format(np.std(measurements0)))
print("Sensor 1 stats:")
print("Mean: {} °C".format(np.mean(measurements1)))
print("Standard Deviation: {} °C".format(np.std(measurements1)))

pylab.hist( , bins=NBins, range=[Min, Max] )
