#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""


def write_file(filename="", text=""):
    """write some text in a given file,
    or create a new one."""
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
