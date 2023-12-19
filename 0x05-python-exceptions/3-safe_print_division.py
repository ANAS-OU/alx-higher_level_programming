#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safe_print_division - a function that divides
    2 integers and prints the result.
    """
    rst = None
    try:
        rst = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(rst))
        return rst
