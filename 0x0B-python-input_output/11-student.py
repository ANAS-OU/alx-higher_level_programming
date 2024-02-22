#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns JSON representation
        of an instance of this class"""
        if attrs is None:
            return self.__dict__

        myJson = {}
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
            if attr in self.__dict__.keys():
                myJson[attr] = getattr(self, attr)
        return myJson

    def reload_from_json(self, json):
        """Method to rebuild this instance"""
        self.__dict__ = json
