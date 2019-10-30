# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 19:01:53 2018

@author: furrukh
"""
#helper function to roll a die
def roll_die():
    import random
    return random.choice([1,2,3,4,5,6,6,6,7])


# Write a function called getAverage(die, numRolls, numTrials), with the following specification:
def getAverage(numRolls,numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """

# A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:
# a dice roll of 1 4 3 has a longest run of 1
# a dice roll of 1 3 3 2 has a longest run of 2
# a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3

# When this function is called with the test case given in the file, it will return 5.312. Your simulation may give slightly different
# values.

# Paste your entire function (including the definition) in the box.

# Restrictions:
# Do not import or use functions or methods from pylab, numpy, or matplotlib.
# Do not leave any debugging print statements when you paste your code in the box.
# If you do not see the return value being printed when testing your function, close the histogram window.
    maxrun_foreachtrial = []
    for j in range(numTrials):
        
        rolls = []
        for i in range(numRolls):
            rolls.append(roll_die())
            consecutive_counts = 1
            maxrun = 0
        for i in range(len(rolls)- 1):
            if rolls[i + 1] == rolls[i]:
                consecutive_counts += 1
            else:
                consecutive_counts = 1
                
            if maxrun < consecutive_counts:
                maxrun = consecutive_counts
                
        if maxrun> 0:
            maxrun_foreachtrial.append(maxrun)
        else:
            maxrun_foreachtrial.append(1)
    
        #print("ROlls",rolls)
        #print("Maxrun:", maxrun)
        
        
        
    print(sum(maxrun_foreachtrial)/numTrials)
    #print(maxrun_foreachtrial)