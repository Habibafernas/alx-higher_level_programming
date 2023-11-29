#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    Args:
        matrix: List of lists containing int or float
        div: number to divide matrix by
    Returns:
        list: List of lists representing divided matrix.
    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """

    if (not isinstance(matrix, list) or matrix == [] or 
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
