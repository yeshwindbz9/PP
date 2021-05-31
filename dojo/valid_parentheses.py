# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 01:29:23 2021

@author: yeshw
"""

"""
Write a function that takes a string of parentheses, and determines 
if the order of the parentheses is valid. The function should return true 
if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""

def valid_parentheses(string):
    """ 
    Checks for valid parentheses. 
  
    Determines if the order of the parentheses is valid. 
  
    Parameters: 
    str: input string containing parentheses.
  
    Returns: 
    bool: output as true if valid or false if it's invalid.
  
    """
    stack = []
    for char in string:
        if char=='(': stack.append('(')
        elif char==')':
            if len(stack)!=0: stack.pop()
            else: return False
    return True if len(stack)==0 else False

print(valid_parentheses.__doc__)
print(valid_parentheses("(())((()())())"))