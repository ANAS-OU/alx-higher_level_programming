#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        new_matrix += list(map(lambda x: x ** 2, arr))
    return (new_matrix)
