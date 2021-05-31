# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:30:58 2021

@author: yeshw
"""

"""
You are given an array(list) strarr of strings and an integer k. 
Your task is to return the first longest string consisting of k consecutive 
strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
Concatenate the consecutive strings of strarr by 2, we get:
treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
              
Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", 
                "abigail"], 2) --> "abigailtheta"
Note:
n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
consecutive strings : follow one after another without an interruption
"""

def longest_consec(strarr, k):
    """ 
    Finds the longest consecutive strings of length k from list strarr. 
  
    Function returns return the first longest string consisting of k consecutive 
    strings taken in the array strarr.
  
    Parameters: 
    list: input list array of strings.
    int: input number k denoting number of consecutive strings.
  
    Returns: 
    string: output longest consecutive word.
    
    """
    longest_word = ""
    for index in range(len(strarr)):
        if len(strarr[index: index+k]) < k or k <= 0: word = ''
        else: word = ''.join(strarr[index: index+k])
        if len(word)>len(longest_word): longest_word = word
    return longest_word

print(longest_consec.__doc__)
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))    