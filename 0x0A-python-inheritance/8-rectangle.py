#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a rectangle class that inherits from BaseGeometry
class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """instantiates the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
