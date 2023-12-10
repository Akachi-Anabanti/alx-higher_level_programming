#!/usr/bin/python3
# Author: Anabanti Akachi

"""An geometry module"""


class Rectangle:
    """Base class"""

    def __init__(self, width, height):
        "instantiates the class"
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "Validates the value"
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
