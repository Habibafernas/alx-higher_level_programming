#!/usr/bin/python3
d = []


def square_matrix_simple(matrix=[]):
    for row in matrix:
        r = list(map(lambda x: x**2, row))
        d.append(r)
    return d
