# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:03:56 2021

@author: yeshw
"""

"""
Consider a sequence u where u is defined as follows:

The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Example:
u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, 
then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) 
returns the element u(n) of the ordered sequence u 
(ordered with < so there are no duplicates) .

Example:
dbl_linear(10) should return 22

Note:
Focus attention on efficiency
"""

def dbl_linear(n):
    """ 
    Finds the nth element in sequence u(n). 
  
    Function finds the nth element in sequence u(n).The number u(0) = 1 is the 
    first one in u. for each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must 
    be in u too. There are no other numbers in u.
  
    Parameters: 
    int: input index.
  
    Returns: 
    int: output element at index n in u.
  
    """
    u = [1]
    a, b = 0, 0
    while(len(u)<=n):
        y = 2 * u[a] + 1
        z = 3 * u[b] + 1
        if z > y: 
            u.append(y)
            a += 1
        elif y > z: 
            u.append(z)
            b += 1
        else:
            u.append(y)
            a += 1
            b += 1
    return u[n]
print(dbl_linear.__doc__)
print(dbl_linear(20))