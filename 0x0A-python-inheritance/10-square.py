#!/usr/bin/python3
"""
Inheritance Module

The purpose of that module is to play around, and
practice the Inheritance Principle in Python.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initialization"""
        super().integer_validator("size", size)
        self.__size = size 

    def area(self):
        """Method computes the square area"""
        return self.__size * self.__size

    def __str__(self):
        """square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
