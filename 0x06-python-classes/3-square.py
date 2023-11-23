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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A method that returns the area of the square
            Returns:
                The area of the square
        """
        return self.__size ** 2
