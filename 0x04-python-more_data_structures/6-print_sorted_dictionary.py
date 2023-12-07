#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    print_sorted_dictionary - a function that
    prints a dictionary by ordered keys
    """
    keys = sorted(a_dictionary)
    for key in keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
