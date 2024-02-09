#!/usr/bin/python3
"""
my calculator module

this simple module contains only one function, add_integer().
"""

def add_integer(a, b=98):
    """
    Returns the addition of two given integers
    """
    # given agrgments must be int or float
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
        
    return int(a) + int(b)