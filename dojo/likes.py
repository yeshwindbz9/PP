# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:12:39 2021

@author: yeshw
"""

"""
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in 
input array, containing the names of people who like an item. 

Example:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) 
# must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases.
"""

def likes(names):
    """ 
    Finds the number of people who have liked a post. 
  
    Function implements the "like" system from Social Networks and other pages. 
    People can "like" blog posts, pictures or other items. This funnction takes
    an input as a list and returns a string of people who liked the post.
  
    Parameters: 
    list: input list of names in string format.
  
    Returns: 
    string: output string of people who liked the post.
  
    """
    if len(names)==0: string = "no one likes this"
    elif len(names)==1: string = f"{names[0]} likes this"
    elif len(names)==2: string = f"{names[0]} and {names[1]} like this"
    elif len(names)==3: string = f"{names[0]}, {names[1]} and {names[2]} like this"
    else: string = f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    return string

print(likes.__doc__)
print(likes(["Alex", "Jacob", "Mark", "Max"]))