# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:44:35 2018

@author: furrukh
"""

# Problem 3-1
# 4.0/4.0 points (graded)
# You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you draw a ball out of the
# bucket, you don't replace it. What is the probability of drawing 3 balls of the same color? Answer the question in reduced fraction
# form - eg 1/5 instead of 2/10.

# 1/7
# correct


# Problem 3-2
# 16.0/16.0 points (graded)
# Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.

# Paste your entire function (including the definition) in the box.

# Restrictions:
# Do not import or use functions or methods from pylab, numpy, or matplotlib.
# Do not leave any debugging print statements when you paste your code in the box.


def drawing_without_replacement_sim(numTrials):
    import random
    success_counter = 0
    for j in range(numTrials):
        bucket = ["R","R","R","R","G","G","G","G"]
        
        
        choices = []
        
        for i in range(3):
            ball = random.choice(bucket)
            #remove the ball from bucket
            choices.append(ball)
            bucket.remove(ball)
        
        print("Choices :", choices, "Bucket :", bucket)
        if choices[0] == choices[1] and choices[1] == choices[2]:
            success_counter += 1
        
        print("counter:", success_counter)
    return success_counter/numTrials