#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return

    new_matrix = []
    for arr in matrix:
        new_matrix += list(map(lambda x: x ** 2, arr))
    return (new_matrix)
