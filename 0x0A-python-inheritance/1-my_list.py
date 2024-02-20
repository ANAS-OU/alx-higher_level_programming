#!/usr/bin/python3
"""
Inheritance Module

The purpose of that module is to play around,
and practice the Inheritance Principle in Python.
"""


class MyList(list):
    """My customized list"""
    def __init__(self, *elements):
        """Initialize the list"""
        for element in elements:
            if type(element) is not int:
                raise TypeError("The list of type int, all its elements must be integers.")

        super().__init__([*elements])

    def append(self, element):
        """Add a new element at the end"""
        if type(element) is not int:
            raise TypeError("The list of type int, new elements must be integers.")
        super().append(element)

    def print_sorted(self):
        """Print the list in ascending order"""
        tmp = super().copy()
        tmp.sort()
        print(tmp)
