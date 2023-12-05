#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    i = 0
    while i < len(my_list):
        c = my_list[i]
        if c in ['c', 'C']:
            my_list.remove(c)
        else:
            i += 1
    my_string = ''.join(my_list)
    return (my_string)
