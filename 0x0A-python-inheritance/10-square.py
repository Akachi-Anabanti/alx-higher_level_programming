#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a square that inherits
from Rectangle """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square which inherits from the 
    Rectangle 
    """

    def __init__(self, size):
        """instantiates with size
        Args:
            size (int): The size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
