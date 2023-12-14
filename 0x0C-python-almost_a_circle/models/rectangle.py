#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a rectangle class that inherits base class"""
from .base import Base


class Rectangle(Base):
    """The Rectangle class
    which inherits the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor

        Args:
            width (int):
            height (int);
            x (int):
            y (int):
        """

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def __width(self):
            """width property getter
            Returns:
                The value of width
            """
            return self.__width

        @__width.setter
        def __width(self, width):
            """width attr setter
            Arg:
            """
            self.__width = width

        @property
        def __height(self):
            """height attr getter"""
            return self.__height

        @__height.setter
        def __height(self, height):
            """height attr setter
            Args:
                height (int):
            """
            self.__height = height

        @property
        def __x(self):
            """x attr getter"""
            return self.__x

        @__x.setter
        def __x(self, x):
            """x attr setter"""
            self.__x = x

        @property
        def __y(self):
            """y attrr getter"""
            return self.__y

        @__y.setter
        def __y(self, y):
            """y attr setter"""

            self.__y = y
