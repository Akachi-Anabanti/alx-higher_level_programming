#!/usr/bin/python3
# Author: Anabanti Akachi

"""An geometry module"""


class BaseGeometry:
    """Base class"""

    def area(self):
        """Area of geometry"""
        raise Exception("area() is not implemented")
