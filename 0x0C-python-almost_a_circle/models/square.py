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
        return "[Square] ({}) {}/{} - {}/{}".format(self.id,
                    self.x, self.y, self.width)

    @property
    def size(self):
        """get the size of the a=square"""
        return self.width

    @setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the class"""
        if args and len(args) != 0:
            self.__init__(self.size, self.x, self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {"id": self.id,
                "width": self.width,
                "x": self.x,
                "y": self.y
                }
