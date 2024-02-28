#!/usr/bin/python3
"""
Base Module

This is a simple module of the porpuse of
being familiar with <Unittest> in python.
"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """Returns list from its JSON representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON representation to file"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as myFile:
            myDict = []
            if list_objs is not None:
                for obj in list_objs:
                    myDict.append(obj.to_dictionary())
            myFile.write(cls.to_json_string(myDict))

    @classmethod
    def create(cls, **dictionary):
        """Returns a new instance"""
        newObj = cls(1)
        newObj.update(**dictionary)
        return newObj

    @classmethod
    def load_from_file(cls):
        """Build list of inctances from a JSON file"""
        filename = cls.__name__ + ".json"
        instances = []

        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as myFile:
            myData = myFile.read()
            dict_list = cls.from_json_string(myData)

        for _dict in dict_list:
            instances.append(cls.create(**_dict))
        return instances
