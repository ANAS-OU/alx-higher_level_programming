#!/usr/bin/python3
"""
Inheritance Module

The purpose of that module is to play around, and
practice the Inheritance Principle in Python.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """Initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method computes the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """rectange description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
