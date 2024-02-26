#!/usr/bin/python3
"""
Base Module

This is a simple module of the porpuse of
being familiar with <Unittest> in python.
"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization with the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation of the class"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON representation to file"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as myFile:
            myDict = []
            if list_objs is not None:
                for obj in list_objs:
                    myDict.append(obj.to_dictionary())
            myFile.write(Base.to_json_string(myDict))
