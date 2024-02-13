#!/usr/bin/python3
"""
Rectangle Module

This module provides a Rectangle class with width and height attributes.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


class Rectangle:
    """Defines a rectange"""    

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with the given width and height."""
        self.width = width
        self.height = height

    @property    
    def width(self):
        """int: The width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
