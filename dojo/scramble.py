# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:25:33 2021

@author: yeshw
"""

"""
Complete the function scramble(str1, str2) that returns true if a portion 
of str1 characters can be rearranged to match str2, otherwise returns false.

Only lower case letters will be used (a-z). No punctuation or digits 
will be included. Performance needs to be considered
Input strings s1 and s2 are null terminated.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

from collections import Counter
def scramble(s1, s2):
    """ 
    Checks if chars of string s2 is present in string s1. 
  
    Function returns true if a portion of str1 characters can be 
    rearranged to match str2, otherwise returns false.
  
    Parameters: 
    str: input string1.
    str: input string2.
  
    Returns: 
    bool: output true for match else false.
  
    """
    s1 = Counter(s1)
    s2 = Counter(s2)
    return all([s2[char]<=s1[char] for char in s2])

print(scramble.__doc__)
print(scramble('rkqodlw', 'world'))