# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:49:27 2021

@author: yeshw
"""

"""
Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, 
how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available 
ingredients (also an object) and returns the maximum number of cakes Pete can 
bake (integer). For simplicity there are no units for the amounts 
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""

def cakes(recipe, available):
    """ 
    Finds the number of cakes that can be made with the recipe and ingredients. 
  
    Function takes the recipe (object) and the available ingredients 
    (also an object) and returns the maximum number of cakes (integer).
  
    Parameters: 
    dict: input dictionary of recipe.
    dict: input dictionary of avaliable ingredients.
  
    Returns: 
    int: output number of cakes that can be baked.
  
    """
    numOfCakes = float('inf')
    for item in recipe:
        if item not in available: return 0
        elif int(available[item]//recipe[item]) < numOfCakes:
            numOfCakes = int(available[item]//recipe[item])
    return numOfCakes

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes.__doc__)
print(cakes(recipe, available))