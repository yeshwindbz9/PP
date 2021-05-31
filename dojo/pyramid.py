# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:08:53 2021

@author: yeshw
"""

"""
Remember the triangle of balls in billiards? To build a classic triangle 
(5 levels) you need 15 balls. With 3 balls you can build a 
2-level triangle, etc.

For more examples,
pyramid(1) == 1
pyramid(3) == 2
pyramid(6) == 3
pyramid(10) == 4
pyramid(15) == 5
Write a function that takes number of balls (≥ 1) and calculates 
how many levels you can build a triangle.
"""

def pyramid(balls):
    """ 
    Determines no of levels that can be built in a pool triangle. 
  
    Function takes number of balls (≥ 1) and calculates 
    how many levels we can build a triangle.
  
    Parameters: 
    int: input number of balls.
  
    Returns: 
    int: output number of levels.
  
    """
    i = 1
    while(True):
        balls -= i
        if balls < 0: return i-1
        elif balls == 0: return i if i>1 else 1
        i += 1
print(pyramid(231))