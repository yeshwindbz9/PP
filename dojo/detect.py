# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:44:18 2021

@author: yeshw
"""

"""
You need to write a function detect that will check if a string starts with 
"Can someone explain", case sensitive. Return true if so, false otherwise.
"""

#detects if a comment starts with "Can someone explain".
def detect(comment):
    return comment.startswith('Can someone explain')

print(detect("Can someone explain to me what this kata is about?"))