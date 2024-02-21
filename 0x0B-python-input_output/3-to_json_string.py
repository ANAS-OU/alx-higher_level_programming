#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""
import json


def to_json_string(my_obj):
    """return a JSON representation
    of a given object"""
    return json.dumps(my_obj)
