# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:18:55 2018

@author: furrukh
"""

def stddeviation(L):
    listlength = len(L)
    if listlength != 0:
        #storing the length of each item in list
        stringlengths = []
        for words in L:
            #print("Lenght is", len(words))
            stringlengths.append(len(words))
        #print(stringlenghts,"sum is", sum(stringlenghts))
        
        mean = sum(stringlengths)/listlength
        #print("mean is", mean)
        variance = 0.0
        for each in stringlengths:
            variance += (each - mean)**2
            
        variance = variance/listlength
        
        deviation = variance**0.5
        
        return round(deviation, 4)
    else:
        return float('NaN')
    
    