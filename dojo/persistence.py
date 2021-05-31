# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:58:16 2021

@author: yeshw
"""

"""
Write a function, persistence, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.

Example:

persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.              
persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.               
persistence(4) => 0   # Because 4 is already a one-digit number.
"""

def persistence(n):
    """ 
    Finds the multiplicative persistence of a number. 
  
    Function takes in a positive parameter num and 
    returns the number of times you must multiply the digits 
    in num until you reach a single digit.
  
    Parameters: 
    int: input positive number.
  
    Returns: 
    int: output multiplicative persistence of input number.
  
    """
    count, res = 0, 1
    while True:
        n = [int(x) for x in str(n)]
        if len(n) == 1: break
        for ele in n: res*=ele
        count +=1
        n, res = res, 1
    return count

print(persistence.__doc__)
print(persistence(999))
        