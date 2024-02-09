#!/usr/bin/python3
"""
matrix module

this simple module contains only one function, add_integer().
"""

def matrix_divided(matrix, div):
    """
    Return a new matrix of all the elements of the taked matrix divided by
    the <div> argument. Should <div> != 0
    """
    # the matrix is a list of lists
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # size of the first sub-list or item
    size = len(matrix[0])
    for item in matrix:
        if type(item) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            for elem in item:
                # each element in our item must be an integer or float
                if type(elem) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(item) != size:
            raise TypeError("Each row of the matrix must have the same size")
    
    # given <div> argument must be an integer or float point
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    

    new_matrix = []
    for _list in matrix:
        new_list = []
        for elem in _list:
            new_list.append(round(elem/div, 2))
        new_matrix.append(new_list)
    
    return new_matrix