# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:01:56 2021

@author: yeshw
"""

"""
The goal of this exercise is to convert a string to a new string where each 
character in the new string is "(" if that character appears only once in the 
original string, or ")" if that character appears more than once in the 
original string. Ignore capitalization when determining if a character 
is a duplicate.
Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""

def duplicate_encode(word):
    """ 
    Encodes duplicate characters. 
  
    Converts a string to a new string where each 
    character in the new string is "(" if that character appears only once in 
    the original string, or ")" if that character appears more than once in 
    the original string. 
  
    Parameters: 
    str: input word or a message to be encoded
  
    Returns: 
    str: output word or a message that is encoded 
  
    """
    word = word.lower()
    wordList = []
    for index in range(len(word)):
        wordList.append(')') if word[index] in word[index+1:] or word[index] in word[:index] else wordList.append('(')
    return "".join(wordList)

print(duplicate_encode.__doc__)
print(duplicate_encode("Success"))