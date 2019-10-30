# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:31:37 2018

@author: furrukh
"""

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        print("i :",i)
        for j in range(N):
            # test bit jth of integer i
            print("j:",j)
            if (i >> j) % 2 == 1:
                
                print("j in if:", j)
                print("i >> j:", i >> j)
                combo.append(items[j])
        yield combo
        
        
 #00000000       