# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:02:02 2021

@author: yeshw
"""

"""
Given an array of integers as strings and numbers, return the 
sum of the array values as if all were numbers.

Example
(sum_mix([9, 3, '7', '3']), 22)
(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)
(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
"""

def sum_mix(arr):
    """ 
    Finds the sum of all numbers in a list in a mixed format. 
  
    Function return the sum of the array 
    (array of integers as strings and numbers) values as if all were numbers. 
  
    Parameters: 
    list: input list of numbers.
  
    Returns: 
    int: output integer that represents of all numbers in the list.
  
    """
    return sum([int(x) for x in arr])