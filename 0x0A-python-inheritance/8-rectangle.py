#!/usr/bin/python3
"""defines a rectangle"""
BaseGeometry = __import__(7-base_geometry.py).BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle"""

    def __init__(self, width, height):
        """initialize a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
