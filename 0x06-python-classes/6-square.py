#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):

        @property
         def size(self):
             return (size.__size)

        @size.sitter
        def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

         def area(self):
            """Return the current area of the square."""
            return (self.__size * self.__size)
