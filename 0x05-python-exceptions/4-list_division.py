#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    list_division - a function that divides
    element by element 2 lists.
    """
    my_list = []
    for i in range(list_length):
        rst = 0
        try:
            rst = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_list.append(rst)
    return my_list
