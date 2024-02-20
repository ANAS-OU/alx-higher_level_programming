#!/usr/bin/python3
"""
Inheritance Module

The purpose of that module is to play around, and
practice the Inheritance Principle in Python.
"""


def inherits_from(obj, a_class):
    """check if an object inherited from
    the given class"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
