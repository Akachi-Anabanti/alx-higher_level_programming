#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that creates a square class"""


class Square:
    """A class that instantiates a private size attribute

    Attributes:
        __size: The size of the square"""

    def __init__(self, size=0):
        """The initialization of the class
            Args:
                size (int, optional): size of square default is 0
        """
        self.size = size

    @property
    def size(self):
        """Returns the value of the private property"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A method that returns the area of the square
            Returns:
                The area of the square
        """
        return self.__size ** 2
