# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:08:02 2021

@author: yeshw
"""

"""
You are given an array of integers
(which will have a length of at least 3, but could be very large). 
The array is either entirely comprised of odd integers or entirely 
comprised of even integers except for a single integer N. Write a method that 
takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):
    """ 
    Identifies the outlier integer from an array. 
  
    Takes the array as an argument and returns its "outlier" int. 
  
    Parameters: 
    list: input integer list
  
    Returns: 
    int: output outlier number
  
    """
    countEven, even, countOdd, odd = 0, 0, 0, 0
    for num in integers:
        if num%2 == 0: 
            countEven +=1
            even = num
        else:
            countOdd +=1
            odd = num
    if countEven > 1:
        return odd
    return even

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))