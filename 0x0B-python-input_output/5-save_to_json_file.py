#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""
import json


def save_to_json_file(my_obj, filename):
    """write on a given file a JSON representation
    of an object"""
    with open(filename, "w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
