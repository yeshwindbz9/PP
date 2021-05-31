# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:24:07 2021

@author: yeshw
"""

"""
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" 
Every time there's an interesting number coming up, 
he notices and then promptly forgets. Who doesn't like catching those 
one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked 
into his car's computer, and we have a box hooked up that reads 
mileage numbers. We've got a box glued to his dash that lights up yellow or 
green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the 
function that parses the mileage number input, and returns a 2 if the number 
is "interesting" (see below), a 1 if an interesting number occurs within the
next two miles, or a 0 if the number is not interesting.
"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or 
more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, 
as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, 
as in 3210.

So, you should expect these inputs and outputs:

# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2

Error Checking
A number is only interesting if it is greater than 99!
Input will always be an integer greater than 0, and less than 1,000,000,000.
The awesomePhrases array will always be provided, and will always be an array, 
but may be empty. (Not everyone thinks numbers spell funny words...)
You should only ever output 0, 1, or 2.
"""

# Checks if the digit is followed by all zeros.
def zeros(number):
    num = set(str(number)[1:])
    return True if len(str(number))>2 and len(num)==1 and '0' in num else False

# Checks if every digit is the same number
def same(number):
    num = set(str(number))
    return True if len(num)==1 and len(str(number))>2 else False

# Checks if the digits are a palindrome: 1221 or 73837
def pallin(number):
    return str(number) == str(number)[::-1] and len(str(number))>2

# Checks if the digits are sequential, incementing†: 1234
def incr(number):
    number = str(number)
    if len(number)<3: return False
    for i in range(len(number)-1):
        if number[i]=='9' and number[i+1]=='0': continue
        elif number[i+1]!=str(int(number[i])+1): return False
    return True

# Checks if the digits are sequential, decrementing‡: 4321
def decr(number):
    number = str(number)
    if len(number)<3: return False
    for i in range(len(number)-1):
        if number[i+1]!=str(int(number[i])-1): return False
    return True

def is_interesting(number, awesome_phrases):
    """ 
    Functions checks for an interesting number of miles.
  
    Function parses the mileage number input, and returns a 2 if the number 
    is "interesting", a 1 if an interesting number occurs within 
    the next two miles, or a 0 if the number is not interesting.
  
    Parameters: 
    int: input integer of miles.
    list: input list of integer miles.
  
    Returns: 
    int: output integer 0, 1 or 2.
  
    """
    if any([zeros(number), same(number), pallin(number), incr(number),
           decr(number), number in awesome_phrases]): return 2
    elif any([zeros(number+1), same(number+1), pallin(number+1), incr(number+1),
           decr(number+1), number+1 in awesome_phrases]): return 1
    elif any([zeros(number+2), same(number+2), pallin(number+2), incr(number+2),
           decr(number+2), number+2 in awesome_phrases]): return 1
    else: return 0
print(is_interesting.__doc__)
print(is_interesting(110, [1337, 256]))