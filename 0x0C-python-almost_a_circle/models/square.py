#!/usr/bin/python3
"""
Base Module

This is a simple module of the porpuse of
being familiar with <Unittest> in python.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization, class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
