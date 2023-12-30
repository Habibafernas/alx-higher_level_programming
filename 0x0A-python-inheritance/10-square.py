#!/usr/bin/python3
"""defines a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size):
        """new sqaure"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

