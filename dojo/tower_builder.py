# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:13:03 2021

@author: yeshw
"""

"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).
Tower block is represented as *

Example:
    A tower of 3 floors looks like below.
[
  '  *  ', 
  ' *** ', 
  '*****'
]
    A tower of 6 floors looks like below.
[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
"""

def tower_builder(n_floors):
    """ 
    Builds a tower of floors represented by *. 
  
    Function takes in a number of floors to construct 
    and return a tower of that many floors representes as *.
  
    Parameters: 
    int: input positive number of floor.
  
    Returns: 
    list: output list of floors represented by *.
  
    """
    tower = []
    space = (n_floors*2)-1
    for i in range(n_floors):
        pattern = '*'*(i+(i+1))
        tower.append(f"{pattern.center(space)}")
    return tower
        
print(tower_builder(3))