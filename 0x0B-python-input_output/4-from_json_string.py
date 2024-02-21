#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""
import json


def from_json_string(my_str):
    """return an object from its JSON
    string representation."""
    return json.loads(my_str)
