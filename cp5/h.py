import numpy as np
import pylab


data = np.genfromtxt("output_temp.txt",dtype=float,delimiter=",",skip_header=1)

time = data[0]
m0 = data[1]
m1 = data[2]

pylab.hist((m0,m1), bins=5, range=[22.75,23.0625] )
pylab.show()
