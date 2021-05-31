# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:57:39 2021

@author: yeshw
"""

"""
Your task in order to complete this Kata is to write a function which formats 
a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just 
returns "now". Otherwise, the duration is expressed as a combination of years, 
days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, separated
by a space.The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). 
Except the last component, which is separated by " and ", just like it would 
be written in English.

A more significant units of time will occur before than a 
least significant one. Therefore, 1 second and 1 year is not correct, but 
1 year and 1 second is.

Different components have different unit of times. So there is not repeated 
units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 
1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function 
should not return 61 seconds, but 1 minute and 1 second instead. Formally, the
 duration specified by of a component must not be greater than any valid more 
 significant unit of time.
"""

def format_duration(seconds):
    """ 
    Formats number of seconds, in a human-friendly way. 
  
    Function accepts a non-negative integer. If it is zero, it just 
    returns "now". Otherwise, the duration is expressed as a combination of years, 
    days, hours, minutes and seconds.
  
    Parameters: 
    int: input seconds.
  
    Returns: 
    str: output string of human-fiendly duration.
  
    """
    year, day, hour, minute = 0, 0, 0, 0
    yearTime, dayTime, hourTime = 60*60*24*365, 60*60*24, 60*60
    if seconds == 0: return "now"
    while seconds >= 60:
        if seconds >= yearTime:
            seconds -= yearTime
            year +=1
        elif seconds >= dayTime:
            seconds -= dayTime
            day += 1
        elif seconds >= hourTime:
            seconds -= hourTime
            hour += 1
        else:
            seconds -= 60
            minute += 1
    year = f"{year} {'years' if year>1 else 'year'}"
    day = f"{day} {'days' if day>1 else 'day'}"
    hour = f"{hour} {'hours' if hour>1 else 'hour'}"
    minute = f"{minute} {'minutes' if minute>1 else 'minute'}"
    seconds = f"{seconds} {'seconds' if seconds>1 else 'second'}"
    time = ', '.join(ele for ele in (year, day, hour, minute, seconds) if ele[0]!='0')
    return ' and'.join(time.rsplit(',', 1))

print(format_duration.__doc__)
print(format_duration(100000000))