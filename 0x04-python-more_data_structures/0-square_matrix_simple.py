#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for r in matrix:
        new_matrix.append(list(map(lambda x: x * x, r)))
    return new_matrix
