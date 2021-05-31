# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:03:29 2021

@author: yeshw
"""

"""
Write a program to determine if a string contains only unique characters. 
Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. 
Characters are case-sensitive, e.g. 'a' and 'A' are 
considered different characters.
"""

def has_unique_chars(string):
  """ 
    Determines if the string contains only unique characters. 
  
    Function accepts a string and checks if the string contains 
    only unique characters string may contain any of the 128 ASCII characters. 
    Characters are case-sensitive, e.g. 'a' and 'A' are considered 
    different characters.
  
    Parameters: 
    str: input string.
  
    Returns: 
    bool: output true/ false.
  
  """
  for char in string:
      if char in string[string.index(char)+1:]: return False
  return True

print(has_unique_chars('abcdef'))