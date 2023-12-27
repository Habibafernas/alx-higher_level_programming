#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """function that prints a square with the character #"""
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
