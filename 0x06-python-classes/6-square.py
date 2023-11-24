#!/usr/bin/python3
# 6-sqaure.py
# Author: Akachi Anabanti
# -*- coding: utf-8 -*-
"""A module that creates a square class"""


class Square:
    """A class that instantiates a private size attribute

    Attributes:
        __size: The size of the square"""

    def __init__(self, size=0, position=(0, 0)):
        """The initialization of the class
            Args:
                size (int, optional): size of square default is 0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the position of the square (x, y)"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of the position
            Args:
                value (tuple): The position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(item, int) for item in value) or
                not all(item >= 0 for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """A method that returns the area of the square
            Returns:
                The area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with #"""

        [print("") for s in range(self.__position[1])]

        for i in range(self.__size):
            [print(" ", end="") for p in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
