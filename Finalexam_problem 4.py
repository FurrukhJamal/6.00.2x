# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:34:41 2018

@author: furrukh
"""
import pylab
import random
values = [1,200]
for i in range(100):
    num1 = random.choice(range(1,100))
    num2 = random.choice(range(1,100))
    values.append(num1+num2)
    #values.append(num2)

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    
    
    pylab.figure()
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.hist(values,bins = numBins)