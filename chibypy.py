



""" 

    https://www.github.com/AutisticAndAshamed/ChiByPy

    This program is free software. It comes without any warranty, to
     * the extent permitted by applicable law. You can redistribute it
     * and/or modify it under the terms of the Do What The Fuck You Want
     * To Public License, Version 2, as published by Sam Hocevar. See
     * http://www.wtfpl.net/ for more details.

"""


def chiplot(xdata, ydata, fitfunction, vars, freevarrange, freevarint, sigma): 
    
    vars = list(vars)
    fit = np.zeros(len(freevarrange))
    chivalue = np.zeros(len(freevarrange))
    

    for i, point in enumerate(freevarrange):
        
        vars[freevarint] = freevarrange[i]
        fit = fitfunction(xdata, *vars)
        dev = ((ydata - fit)**2) / sigma ** 2
        chivalue[i] = np.sum(dev)

    chimin = np.min(chivalue)
    variablevalue = freevarrange[np.where(chivalue == float(chimin))]

    searchprecision = 0
    while True:
        uncertainty = freevarrange[np.where(abs(chimin + 1 - chivalue) < searchprecision)]
        searchprecision += 1e-3 * np.mean(np.diff(freevarrange))
        if len(uncertainty) == 2:
            break
        elif len(uncertainty) > 2:
            print('Error: returned incorrect number of uncertainty values')
            break
    uncertainty = uncertainty - variablevalue

    return chivalue, chimin, variablevalue, uncertainty
