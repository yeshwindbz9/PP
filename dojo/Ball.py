# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:10:18 2021

@author: yeshw
"""

"""
Create a class Ball. Ball objects should accept one argument for 
"ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a 
"ball type" of "regular."

Examples:
Ball().ball_type  => regular
Ball("super").ball_type => super
"""

class Ball(object):
    #initializes the ball object with ball_type
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

print(Ball().ball_type)