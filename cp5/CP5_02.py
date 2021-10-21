from DAH import DS18B20
import pylab
import matplotlib.animation as animation
import time

# Readout temperature sensor
tmp0 = DS18B20( address="10-00080379b4fb" )

# Empty arrays of time and measurement values to plot
timeValues = [ ]
measurements = [ ]

# Set up the plot object
plotFigure = pylab.figure()

# The function to call each time the plot is updated
t0 = time.time()
def updatePlot( i ):
  
    timeValues.append( time.time() -t0) # Store time
    measurements.append( tmp0.getCelsius())           # Store temperature
    plotFigure.clear()# Clear the old plot
    pylab.plot( timeValues, measurements ) # Make the new plot
    pylab.title("Temperature Variation as a Function of Time")   
    pylab.xlabel("Time (s)")
    pylab.ylabel("Temperature (°C)")
# Make the animated plot
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=1000,frames=50 )

pylab.show()
