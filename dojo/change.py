# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:47:28 2021

@author: yeshw
"""

"""
Here we will work with strings like the string data above and 
not with files.

The function change(s, prog, version) given:

s=data, prog="Ladder" , version="1.1" will return:

"Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 
Version: 1.1"

Rules:

The date should always be "2019-01-01".

The author should always be "g964".

Replace the current "Program Title" with the prog argument supplied to 
your function. Also remove "Title", so in the example case 
"Program Title: Primes" becomes "Program: Ladder".

Remove the lines containing "Corporation" and "Level" completely.

Phone numbers and versions must be in valid formats.

A valid version in the input string data is one or more digits 
followed by a dot, followed by one or more digits. So 0.6, 5.4, 
14.275 and 1.99 are all valid, but versions like .6, 5, 14.2.7 and 
1.9.9 are invalid.

A valid input phone format is +1-xxx-xxx-xxxx, where each x is a digit.

If the phone or version format is not valid, 
return "ERROR: VERSION or PHONE".

If the version format is valid and the version is anything other than 2.0, 
replace it with the version parameter supplied to your function. 
If it’s 2.0, don’t modify it.

If the phone number is valid, replace it with "+1-503-555-0090".
"""

import re
def change(s, prog, version):
    """ 
    Filters data by matching and substituting. 
  
    Function takes data, program title and version as input 
    and filters and substitute elements from data to return the
    correct format.
  
    Parameters: 
    str: input string data
    str: input string program title
    str: input string version
  
    Returns: 
    str: output formatted data.
  
    """
    s = list(s.split('\n'))
    for i in range(len(s)):
        if "Program" in s[i]: s[i] = f"Program: {prog} "
        elif "Author" in s[i]: s[i] = "Author: g964 "
        elif "Phone" in s[i]:
            phone = s[i].split()[1]
            pattern = "\+1-\d{3}-\d{3}-\d{4}"
            match = re.search(pattern, phone)
            if not match:
                return "ERROR: VERSION or PHONE"
                break
            s[i]="Phone: +1-503-555-0090 "
        elif "Corporation" in s[i]: s[i] = ''
        elif "Date" in s[i]: s[i] = "Date: 2019-01-01 "
        elif "Version" in s[i]:
            ver = s[i].split()[1].split('.')
            if len(ver)!=2 or '' in ver:
                return "ERROR: VERSION or PHONE"
                break
            if ver == ['2', '0']: s[i] = "Version: 2.0"
            else: s[i] = f"Version: {version}"
        elif "Level" in s[i]: s[i] = ''
    else:
        return ''.join(s)
    
s = """Program title: Primes\nAuthor: Kern\n
Corporation: Gold\nPhone: +1-503-555-0091\n
Date: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha
"""
prog = "Ladder"
version = "1.1"
print(change(s, prog, version))