#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""


def append_write(filename="", text=""):
    """append text to the given file,
    or create a new one."""
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
