# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:28:36 2021

@author: yeshw
"""

"""
There is a narrow hallway in which people can go right and left only. 
When two people meet in the hallway, by tradition they must salute each other. 
People move at the same speed left and right.

Your task is to write a function that, given a string representation of 
people moving in the hallway, will count the number of salutes that 
will occur.
Note: 2 salutes occur when people meet, one to the other and vice versa.

Input
People moving right will be represented by >; people moving left 
will be represented by <. An example input would be >--<--->->. 
The - character represents empty space, which you need not worry about.

Examples
Input: >----->-----<--<
Output: 8

Explanation: Both guys moving right will meet both guys moving left.
Hence a total of 4 meetings will occur and 8 salutes will occur.

Input: <---<--->----<
Output: 2

Explanation: Only one meeting occurs.
"""

def count_salutes(hallway):
    """ 
    Counts the number of salutes given in a hallway. 
  
    Function, given a string representation of 
    people moving in the hallway, will return the number of salutes that 
    will occur.
  
    Parameters: 
    str: string representation of people moving in the hallway
  
    Returns: 
    int: output number of salutes.
  
    """
    fromRight, salute = 0, 0
    for people in hallway:
        if people == '>': fromRight += 1
        elif people == '<' and fromRight>0: salute += 2*fromRight
    return salute

print(count_salutes.__doc__)
print(count_salutes(">--->---<--<"))