# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:53:09 2021

@author: yeshw
"""

"""
In this simple exercise, you will create a program that will take two lists 
of integers, a and b. Each list will consist of 3 positive integers above 0, 
representing the dimensions of cuboids a and b. You must find the difference 
of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume 
of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.
"""
import math
def find_difference(a, b):
    """ 
    Finds the difference of the cuboids' volumes regardless of which is bigger. 
  
    Program takes two lists of integers, a and b. Each which consist of 3 
    positive integers above 0,representing the dimensions of cuboids a and b and 
    returns the difference of the cuboids' volumes regardless of which is bigger.
  
    Parameters: 
    list: input list of dimensions of cuboid a.
    list: input list of dimensions of cuboid b.
  
    Returns: 
    int: output absolute difference.
  
    """
    return abs(math.prod(a) - math.prod(b))

print(find_difference([3, 2, 5], [1, 4, 4]))