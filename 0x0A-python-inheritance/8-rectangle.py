#!/usr/bin/python3
"""
Inheritance Module

The purpose of that module is to play around, and
practice the Inheritance Principle in Python.
"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
