#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a class Sqaure that inherits the rectangle
class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the value of the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the class attributes"""

        attributes = ["id", "size", "x", "y"]

        if args:
            for attr, val in zip(attributes, args):
                setattr(self, attr, val)
        if kwargs:
            for attr, val in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, val)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.width)
