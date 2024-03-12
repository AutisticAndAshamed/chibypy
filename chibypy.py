



""" 
    https://www.github.com/AutisticAndAshamed/ChiByPy

    This program is free software. It comes without any warranty, to
     * the extent permitted by applicable law. You can redistribute it
     * and/or modify it under the terms of the Do What The Fuck You Want
     * To Public License, Version 2, as published by Sam Hocevar. See
     * http://www.wtfpl.net/ for more details.

"""


def chiplot(xdata, ydata, sigma, fitfunction, vars, freevarrange, freevarint): 
    
    vars = list(vars)
    fit = numpy.zeros(len(freevarrange))
    chivalue = numpy.zeros(len(freevarrange))
    

    for i in enumerate(freevarrange):
        
        vars[freevarint] = freevarrange[i]
        fit = fitfunction(xdata, *vars)
        dev = ((ydata - fit)**2) / sigma ** 2
        chivalue[i] = numpy.sum(dev)

    chimin = numpy.min(chivalue)
    variablevalue = freevarrange[numpy.where(chivalue == float(chimin))]

    uncertainty_indices = numpy.argsort(numpy.abs(chivalue - (chimin + 1)))[:2]
    uncertainty = numpy.sort(freevarrange[uncertainty_indices] - variablevalue)

    return chivalue, variablevalue, uncertainty

