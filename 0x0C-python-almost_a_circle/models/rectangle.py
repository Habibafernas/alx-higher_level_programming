#!/usr/bin/python3
"""Defines a model"""
from models.base import Base


class Rectangle(Base):
    """defines a class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise a new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """get the x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """represents the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        """return the dimentions"""
        return"[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)


    def update(self, *args, **kwargs):
        """update to the class"""
        if args and len(args) != 0:
            self.__init__(self.width, self.height, self.x, self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
