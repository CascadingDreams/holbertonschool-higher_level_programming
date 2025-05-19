#!/usr/bin/python3
'''
Module for adding integers.
Adds two integers.
'''

def add_integer(a, b=98):
    '''
    Adds two integers and returns the result.
    
    Args: 
        a (int or float): first num to add
        b (int or float): second num to add
        
    Returns:
        int: Adding a and b
    
    Raises:
        TypeError: if a and/or b not an int or float
    '''
    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")
    
    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")
    
    return a + b
