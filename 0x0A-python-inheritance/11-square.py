#!usr/bin/python3
"""defines a square"""
Rectangle = __ import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self, size):
        """get the area"""
        return self.__width * self.__height

    def __str__:
        """return s"""
        s = "[" + str(self.__class__.__name__) + "]"
        s += str(self.__width) + "/" + str(self.__height)
        return s
