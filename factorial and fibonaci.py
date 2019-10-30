# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:08:28 2018

@author: furrukh
"""

def factorial_loop(n):
    factorial = 1
    count = 0
    while n > 0:
        count += 1
        factorial *= n
        n -= 1
    
    return "Factorial of " + str(n + count) + " is " + str(factorial)

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
    
    
def fib_loop(n):
    fibonacci = [0, 1]
    
    for i in range(2, n + 1):
        nextfibnum = fibonacci[i - 2] + fibonacci[i - 1]
        fibonacci.append(nextfibnum)
    
    print (fibonacci[0:])
    return fibonacci[n]


def fib_recur(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib_recur(n - 2) + fib_recur(n - 1)


def fib_dynamic(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_dynamic(n - 2) + fib_dynamic(n - 1)
        memo[n] = result
        return result
    

