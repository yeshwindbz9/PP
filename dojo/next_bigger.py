# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:51:11 2021

@author: yeshw
"""

"""
Create a function that takes a positive integer and returns the next bigger 
number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, 
return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
"""

def next_bigger(n):
    """ 
    Gives the next bigger number that can be formed by rearranging its digits. 
  
    Function accepts a positive integer and returns the next bigger 
    number that can be formed by rearranging its digits.
  
    Parameters: 
    int: input number.
  
    Returns: 
    int: output next biggest number.
  
    """
    try:
        digits = list(str(n))
        size = len(digits)
        pivot = next(i for i in reversed(range(size-1)) if digits[i] < digits[i+1])
        swap  = next(i for i in reversed(range(size)) if digits[pivot] < digits[i])
    
        digits[pivot], digits[swap] = digits[swap], digits[pivot]
        digits[pivot+1:] = reversed(digits[pivot+1:])
        return int(''.join(d for d in digits))
    except:
        return -1

    return int(''.join(d for d in digits))

print(next_bigger(1550))
#[5, 8, 8, 4, 6, 4, 3, 6, 1, 0, 0, 5] [5, 8, 8, 4, 6, 4, 3, 6, 1, 0, 5, 0]