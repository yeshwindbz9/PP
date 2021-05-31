# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:30:55 2021

@author: yeshw
"""

"""
You are a sheep farmer, and are now plagued by wolves which 
pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten. 
Remember that you are standing at the front of the queue which is 
at the end of the array:

[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE)
   7      6      5      4      3            2      1
If the wolf is the closest animal to you, 
return "Pls go away and stop eating my sheep". 
Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" 
where N is the sheep's position in the queue.

Note: there will always be exactly one wolf in the array.

Examples
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"
"""

def warn_the_sheep(queue):
    """ 
    Warns the sheep in front of the wolf that it is about to be eaten. 
  
    Function accepts a list and if the wolf is the closest animal to you, 
    returns "Pls go away and stop eating my sheep". Otherwise, 
    returns "Oi! Sheep number N! You are about to be eaten by a wolf!" 
    where N is the sheep's position in the queue.
  
    Parameters: 
    list: input list of positions of sheeps and wolf.
  
    Returns: 
    str: output string warning.
  
    """
    wolfAt = queue.index('wolf')
    N = len(queue) - wolfAt - 1
    if wolfAt == len(queue)-1: return "Pls go away and stop eating my sheep"
    else: return f"Oi! Sheep number {N}! You are about to be eaten by a wolf!"

print(warn_the_sheep.__doc__)
print(warn_the_sheep(['sheep', 'wolf', 'sheep']))