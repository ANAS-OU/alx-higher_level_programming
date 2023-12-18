#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    safe_print_list - a function that prints <x>
    element of <my_list>
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1

        except IndexError:
            break

    print()
    return count
