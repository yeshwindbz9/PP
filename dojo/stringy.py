# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:39:31 2021

@author: yeshw
"""

"""
Write me a function stringy that takes a size and returns a string of 
alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
"""

def stringy(size):
    """ 
    Produces a string of alternating '1s' and '0s'. 
  
    Function accepts a (int) size and returns a string of 
    alternating '1s' and '0s' such that the string starts with a 1.
  
    Parameters: 
    int: input size.
  
    Returns: 
    str: output string of alternating '1s' and '0s'.
  
    """
    string = ['1']
    for i in range(1,size):
        if string[i-1]=='1': string.append('0')
        else: string.append('1')
    return '' if size==0 else ''.join(string)

print(stringy.__doc__)
print(stringy(5))