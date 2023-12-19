#!/usr/bin/python3

"""
Writing an empty class Square
that defines a square

"""


class Square:
    """ Class Attributes """
    __size = 0

    def __init__(self, size=0):
        """ Instantiation """
        if size:
            self.__size = size
