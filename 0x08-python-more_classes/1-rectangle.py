#!/usr/bin/python3
"""
Rectangle Module

This is just a simple module that provides a rectangle class
with width and height attributes.
"""


class Rectangle:
    """Defines a rectange
    """    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property    
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value