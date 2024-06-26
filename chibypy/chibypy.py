



""" 
    https://www.github.com/AutisticAndAshamed/ChiByPy

    This program is free software. It comes without any warranty, to
     * the extent permitted by applicable law. You can redistribute it
     * and/or modify it under the terms of the Do What The Fuck You Want
     * To Public License, Version 2, as published by Sam Hocevar. See
     * http://www.wtfpl.net/ for more details.

"""
import numpy as np
from scipy.optimize import curve_fit

def chiplot(xdata, ydata, fitfunction, vars, freevarrange, freevarint, sigma): 
    vars = list(vars)
    chivalue = np.zeros(len(freevarrange))
    

    for i, point in enumerate(freevarrange):
        
        vars[freevarint] = freevarrange[i]
        fit = fitfunction(xdata, *vars)
        dev = ((ydata - fit)**2) / sigma ** 2
        chivalue[i] = np.sum(dev)

    chimin = np.min(chivalue)
    variablevalue = freevarrange[np.where(chivalue == float(chimin))]

    uncertainty_indices = np.argsort(np.abs(chivalue - (chimin + 1)))[:2]
    uncertainty = np.sort(freevarrange[uncertainty_indices] - variablevalue)
    
    return chivalue, chimin, variablevalue, uncertainty

def errorflatten(datax, datay, sigmax, sigmay):
    def linearfit(x, m, b):
        return m * x + b

    yerror = sigmay
    for i in range(10000):
        popt, pcov = curve_fit(linearfit, datax, datay, sigma = yerror)

        m = popt[0]
        yerrorstar = m * sigmax
        yerror = np.sqrt(sigmay**2 + yerrorstar**2)


    return yerror