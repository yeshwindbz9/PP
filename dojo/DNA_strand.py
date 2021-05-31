# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:36:38 2021

@author: yeshw
"""

"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of 
cells and carries the "instructions" for the development and 
functioning of living organisms.


In DNA strings, symbols "A" and "T" are complements of each other, as 
"C" and "G". You have function with one side of the DNA 
(string, except for Haskell); you need to get the other complementary side. 
DNA strand is never empty or there is no DNA at all 
(again, except for Haskell).

Examples
DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"
"""

def DNA_strand(dna):
    """ 
    Completes the complimentary side of the DNA. 
  
    Function takes one side of the DNA produces and returns the
    complimentary side of the DNA. 
  
    Parameters: 
    str: input string one side of the DNA.
  
    Returns: 
    str: output other complimentary side of the DNA.
  
    """
    strands = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    compSide = [strands[alpha] for alpha in dna]
    return ''.join(compSide)

print(DNA_strand.__doc__)
print(DNA_strand("GTAT"))