#!/usr/bin/python3
"""
Inheritance Module

The purpose of that module is to play around, and
practice the Inheritance Principle in Python.
"""


class BaseGeometry:
    """Geometry Class"""
    def area(self):
        """Area Method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validate <value> argument"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
