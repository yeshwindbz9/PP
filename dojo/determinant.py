# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:51:04 2021

@author: yeshw
"""

"""
Write a function that accepts a square matrix (N x N 2D array) and 
returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start 
with the smallest cases:

A 1x1 matrix |a| has determinant a.

A 2x2 matrix [ [a, b], [c, d] ] or

|a  b|
|c  d|
has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by reducing the problem 
to the calculation of the determinants of n matrices ofn-1 x n-1 size.

For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

|a b c|  
|d e f|  
|g h i|  
the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) 
where det(a_minor) refers to taking the determinant of the 2x2 matrix created 
by crossing out the row and column in which the element a occurs:

|- - -|
|- e f|
|- h i|  
Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 
4x4 matrix with first row [a, b, c, d], then:

det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
"""

def tabulate(A):
    """ 
    Finds cofactors and determinant of a NxN matrix where N>2. 
  
    Function returns the determinant of an n x n for n>2 sized matrix which is 
    calculated by reducing the problem to the calculation of the determinants 
    of n matrices ofn-1 x n-1 size.
  
    Parameters: 
    list: input NxN Matrix.
  
    Returns: 
    float: output determinant value.
  
    """
    subs = [[row[:x] + row[x + 1:] for row in A[1:]] for x in range(len(A[0]))]
    det = 0
    sign = 1
    for i in range(len(A[0])):
        n_d = determinant(subs[i])
        det += sign * A[0][i] * n_d
        sign *= -1
    return det


def determinant(A):
    """ 
    Finds Determinant of a NxN matrix. 
  
    Function returns the determinant of an n x n sized matrix which is 
    calculated by reducing the problem to the calculation of the determinants 
    of n matrices ofn-1 x n-1 size.
  
    Parameters: 
    list: input NxN Matrix.
  
    Returns: 
    float: output determinant value.
  
    """
    det=0
    if len(A) == 1:
        return A[0][0]
    elif len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        det = tabulate(A)
    return det



m1  = [[1]]
m2 = [ [1, 3], [2,5]]
m3 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant.__doc__)
print(determinant(m3))