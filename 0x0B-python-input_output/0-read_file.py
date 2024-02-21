#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""


def read_file(filename=""):
    """Write a readed file to the stdout"""
    with open(filename, "r", encoding="utf-8") as myFile:
        data = myFile.read()
        print(data, end="")
