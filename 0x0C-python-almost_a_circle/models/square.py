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

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.width)
