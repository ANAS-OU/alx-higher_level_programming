#!/usr/bin/python3
"""
File Module

This is just a simple module, the popuse of it
is to be familiar with files (input/output) in python
"""

import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
myObject = []

if os.path.exists(filename):
    myObject = load_from_json_file(filename)

for item in sys.argv[1:]:
    myObject.append(item)

save_to_json_file(myObject, filename)
