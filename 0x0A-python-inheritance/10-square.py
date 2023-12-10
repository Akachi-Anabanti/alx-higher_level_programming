#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a square class that inherits
from Rectangle class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """instantiates the class with size
        Args:
            size (int): The size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
