#!/usr/bin/python3
"""defines a square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a class"""

    def __init__(self, size, x=0, y=0, id=None):
        """defines the square"""
        super().__init__(size, size, x, y, id)

     def __str__(self):
        """Return the dimentions."""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id. self.x, self.y, self.width)
