#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    uniq_add - a function that adds all unique
    integers in a list
    """
    rst = 0
    new_list = set(my_list)
    for elemnet in new_list:
        rst += elemnet
    return (rst)
