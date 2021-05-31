# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:15:56 2021

@author: yeshw
"""

"""
Professor Chambouliard hast just discovered a new type of magnet material. 
He put particles of this material in a box made of small boxes arranged in K 
rows and N columns as a kind of 2D matrix K x N where 
K and N are postive integers. He thinks that his calculations show that the 
force exerted by the particle in the small box (k, n) is:

v(k, n) = \frac{1}{k(n+1)^{2k}}
The total force exerted by the first row with k = 1 is:

u(1, N) = \sum_{n=1}^{n=N}v(1, n) = \frac{1}{1.2^2} + 
    \frac{1}{1.3^2}+...+\frac{1}{1.(N+1)^2}
We can go on with k = 2 and then k = 3 etc ... and consider:

S(K, N) = \sum_{k=1}^{k=K}u(k, N) = \sum_{k=1}^{k=K}(\sum_{n=1}^{n=N}v(k, n)) 
 => (doubles(maxk, maxn))
Task:
To help Professor Chambouliard can we calculate the function doubles that will 
take as parameter maxk and maxn such that doubles(maxk, maxn) = S(maxk, maxn)? 
Experiences seems to show that this could be something around 0.7 when 
maxk and maxn are big enough.

Examples:
doubles(1, 3)  => 0.4236111111111111
doubles(1, 10) => 0.5580321939764581
doubles(10, 100) => 0.6832948559787737
Notes:
In u(1, N) the dot is the multiplication operator.
Don't truncate or round: Have a look at "assertFuzzyEquals" in "RUN EXAMPLES".
"""

def doubles(maxk, maxn):
    """ 
    Finds the force exerted by the magnetice particle in the small box. 
  
    Function will take as parameters maxk and maxn and return S(maxk, maxn), 
    where Σk(1,maxk)Σn(1, maxn)1/(k*((n+1)**(2*k)))
  
    Parameters: 
    int: input maxk.
    int: input maxn.
  
    Returns: 
    float: output float magnetic force S(maxk, maxn).
  
    """
    total = 0
    for k in range(1, maxk+1):
        for n in range(1, maxn+1):
            total += (n+1)**(-2*k)/k
    return total

print(doubles.__doc__)
print(doubles(10, 10000))