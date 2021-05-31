# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:13:16 2021

@author: yeshw
"""

"""
Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the 
input string. The input string can be assumed to contain only alphabets 
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""
def duplicate_count(text):
    """ 
    Counts duplicate characters. 
  
    Counts the number of distinct case-insensitive alphabetic characters 
    and numeric digits that occur more than once in the input string. 
  
    Parameters: 
    str: input word or a message 
  
    Returns: 
    int: output count of the number of distinct characters 
  
    """
    text = text.lower()
    count = 0
    textSet = set(text)
    for let in textSet:
        if text.count(let) > 1: count += 1
    return count

print(duplicate_count.__doc__)
print(duplicate_count('aA11'))