# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:31:05 2020
@author: yeshw
"""
import math

def isPowerOf10(n):
    '''
        the function takes a number as input and
        returns true if the number is a power of 10
    '''
    s = math.log(n,10)
    p = round(s)
    return (10**p) == n

def findNumOfDigits(n):
    ''''
        the function takes a number as input and 
        returns the number of digits as its output
    '''
    
    #calculates the number of digits
    dig = math.ceil((math.log(n)/math.log(10)))
    #checking if n is a power of 10
    if isPowerOf10(n):
        #adding 1 is n is a power of 10
        dig += 1
    return dig

#converting the input to a list
ipList = [100,1000,10000,100000,1000000]
# initialising the output list for printing
grid = [[0 for _ in range(5)] for i in range(5)]
#counter for each row
i = 0
#computing results for each list element
for num in ipList:
    grid[i][0] = findNumOfDigits(num**2)
    grid[i][1] = findNumOfDigits(num**3)
    grid[i][2] = findNumOfDigits(2**num)
    grid[i][3] = findNumOfDigits(math.factorial(num))
    grid[i][4] = findNumOfDigits(num**num)
    i += 1   
#writing outputs to a file    
with open('output.txt','w') as file:
    for line in grid:
        for numbers in line:
            fixed_string = "{0:>9}".format(str(numbers))
            file.write(f'{fixed_string}')
        file.write('\n')
print('results are printed in the output file')
'''
#test
n =math.factorial(1000000)
print(findNumOfDigits(n))
'''