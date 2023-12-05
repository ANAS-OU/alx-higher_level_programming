#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for c in ['c', 'C']:
        if c in my_list:
            my_list.remove(c)
    my_string = ''.join(my_list)
    return (my_string)
