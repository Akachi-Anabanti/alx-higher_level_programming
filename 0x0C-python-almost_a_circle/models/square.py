#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a class Sqaure that inherits the rectangle
class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.width)
