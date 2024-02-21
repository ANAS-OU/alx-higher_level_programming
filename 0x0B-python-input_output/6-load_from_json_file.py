#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""
import json


def load_from_json_file(filename):
    """return a created object from its representation
    readed from the given file"""
    with open(filename, "r", encoding="utf-8") as myFile:
        return json.load(myFile)
