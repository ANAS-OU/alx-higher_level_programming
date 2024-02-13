#!/usr/bin/python3
"""
Rectangle Module

A simple module
"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with the given width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of Rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter Method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method for height""" 
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value

    def area(self):
        """Rectongale area"""
        return self.__width * self.__height

    def perimeter(self):
        """Rectongale perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Method String Object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ('#' * self.__width)
