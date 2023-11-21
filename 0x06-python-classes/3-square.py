#!/usr/bin/python3


"""Defines a class"""


class Square:
    """initialises a square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area"""

        return (self.__size * self.__size)
