#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return

    return (list(list(map(lambda x: x ** 2, arr)) for arr in matrix))
