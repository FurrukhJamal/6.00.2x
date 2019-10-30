# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:19:04 2018

@author: furrukh
"""

def greedysum(L, s):
     multipliers = []
    remain = s
    for i in L:
        if i <= remain:
            mult = remain // i
            multipliers.append(mult)
            remain -= i * mult
        else:
            multipliers.append(0)
    sum1 = 0
    for j in range(len(multipliers)):
        sum1 += L[j]*multipliers[j]
    if sum1 == s:
        return sum(multipliers)
    else:
        return 'no solution'
    
    
    
    
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    
    max_ending_here = max_so_far = L[0]
    for i in L[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


