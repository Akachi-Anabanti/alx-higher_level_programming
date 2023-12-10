#!/usr/bin/python3
# Author: Anabanti Akachi

"""An geometry module"""


class BaseGeometry:
    """Base class"""

    def area(self):
        """Area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "Validates the value"
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

