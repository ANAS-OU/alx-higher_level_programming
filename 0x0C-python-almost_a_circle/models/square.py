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

    def update(self, *args, **kwargs):
        """Method for updating an instance"""
        if len(args) > 0:
            if len(args) >= 2:
                args = [*args[:2], *args[1:]]
            keys = list(self.__dict__.keys())
            idx = 0
            for arg in args:
                key = keys[idx]
                self.__dict__[key] = arg
                idx += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}

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
