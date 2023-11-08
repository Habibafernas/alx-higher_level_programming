#!/usr/bin/python3

d = []
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for c in row:
            d[c]= (matrix[c]) ** 2
    return d
