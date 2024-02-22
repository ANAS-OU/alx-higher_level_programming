#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""


def class_to_json(obj):
    """returns JSON serialization
    of a given object"""
    return obj.__dict__
