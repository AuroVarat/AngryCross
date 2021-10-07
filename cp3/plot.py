import pylab
x = [3.139889216474582, 1.582250130821559, 0.08748370273794005, 0.052790081713158625]
y=[3.20, 1.60, 0.08, 0.04]

pylab.plot(x,y)
pylab.xlabel('Measured ADC Voltages (V)')
pylab.ylabel('Input Voltages (V)')
pylab.title('Calibration Graph')
pylab.grid(True)
pylab.savefig("plot.pdf")
pylab.show()
