#!/usr/bin/python3
"""defines a rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """returns the dimentions"""
        s = "[" + str(self.__class__.__name__) + "]"
        s += str(self.__width) + "/" + str(self.__height)
        return s
