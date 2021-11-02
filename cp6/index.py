"""
Checkpoint 6 - DAH 
Auro Varat Patnaik
28th October 2021
"""

import math
from numpy.core.fromnumeric import searchsorted
import pylab as pl
import numpy as np
from scipy.optimize import curve_fit


def gauss(x,a,b,c,d):
    """
    Define function to fit, (linear)
    """
   
    return a*np.exp(-((x-b)**2)/((2*c**2))) + d
def local_peak_finder(binedges,entries,mini,maxi):    
    min_index = np.searchsorted(binedges, mini)
    max_index = np.searchsorted(binedges, maxi)
    bins = binedges[min_index:max_index]
    entry = entries[min_index:max_index]
    peak = binedges[min_index:max_index][np.argmax(entry)]
    return peak,bins,entry
def gaussian_fit(x,y,estimates):
     #      Estimate of peak location and height
    peakheight = np.amax(y)                   # Peak value
    peakloc = x[np.argmax(y)]            # Peak locaion
    
    # Do a fit using curve_fit, note retuns two lists. 
    popt,pcov = curve_fit(gauss,x,y,p0=estimates)

    perr = np.sqrt(np.diag(pcov))        # Errors

    #    Print out the results, popt contains fitted vales and perr the errors
    print("a is : {0:10.5e} +/- {1:10.5e}".format(popt[0],perr[0]))
    print("b is : {0:10.5e} +/- {1:10.5e}".format(popt[1],perr[1]))
    print("c is : {0:10.5e} +/- {1:10.5e}".format(popt[2],perr[2]))
    print("d is : {0:10.5e} +/- {1:10.5e}".format(popt[3],perr[3]))

    pl.subplot(2,1,1)
    pl.errorbar(x,y,xerr=0.0,yerr=0.0,fmt="bx")     # Plot the data
    #      Plot the 
    pl.plot(x,gauss(x,*popt),"r")

    #       Label the graph
    pl.title("Guassian Fit pk: {0:8.4g} loc: {1:8.4g} w: {2:8.4g}".format(popt[0],popt[1],popt[2]))
    pl.xlabel("Invariant Mass "+r'${GeV/c^2}$')
    pl.ylabel("Count")

    #    Add residuals
    pl.subplot(2,1,2)
    pl.errorbar(x,gauss(x,*popt) - y,xerr = 0.0, yerr =0.0,fmt = "rx")
    pl.xlabel("Invariant Mass "+r'${GeV/c^2}$')
    pl.ylabel("Count residual")
    pl.show()
def main():

    data = np.genfromtxt("upsilons-mass-xaa.txt", dtype=float)
    entries, binedges,patches = pl.hist(data, bins=170, range=[8.48, 11],color='orchid')

    pl.title("Invariant Mass of Muon Pairs")
    pl.xlabel("Invariant Mass "+r'${GeV/c^2}$')
    pl.ylabel("Count")
    #pl.show()
  
    # First Peak using Estimate
    first_peak,x_first,y_first = local_peak_finder(binedges,entries,9.3,9.6)
    second_peak,x_second,y_second = local_peak_finder(binedges,entries,9.9,10.1)
    third_peak,x_third,y_third = local_peak_finder(binedges,entries,10.25,10.45)
    print("Visual Estimate mean of Peak Event")
    print("Mean of the Peak: {0} , Unbiased Variance: {1} , Standard Deviation: {2} ".format(str(np.mean(x_first)),str(np.var(x_first,ddof=1)),str(np.std(x_first))))
    print("Gaussian Fits SciPy")
    # gaussian_fit(x_first,y_first,[2660,9.4,0.04,500])
    # gaussian_fit(x_second,y_second,[910,10,0.06,400])
    # gaussian_fit(x_third,y_third,[571,10.3,0.08,350])
    print(np.sum(y_first))

    
if __name__ == "__main__":
    main()