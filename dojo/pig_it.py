# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:44:56 2021

@author: yeshw
"""

"""
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    """ 
    Converts a given sentence into pig latin. 
  
    Function moves the first letter of each word to the end of it, 
    then add "ay" to the end of the word. Leave punctuation marks untouched. 
  
    Parameters: 
    str: input sentence in english.
  
    Returns: 
    str: output sentence in pig latin.
  
    """
    words = [word[1:]+word[0]+"ay" if word.isalpha() else word for word in text.split(' ')]
    return ' '.join(words)
        
print(pig_it.__doc__)
print(pig_it('Pig latin is cool'))