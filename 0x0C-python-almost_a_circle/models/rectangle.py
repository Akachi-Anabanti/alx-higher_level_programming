#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a rectangle class that inherits base class"""
from models.base import Base


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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """width property getter
            Returns:
                The value of width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """width attr setter
            Arg:
            """
            self.__width = value

        @property
        def height(self):
            """height attr getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """height attr setter
            Args:
                height (int):
            """
            self.__height = value

        @property
        def x(self):
            """x attr getter"""
            return self.__x

        @x.setter
        def x(self, value):
            """x attr setter"""
            self.__x = value

        @property
        def y(self):
            """y attrr getter"""
            return self.__y

        @y.setter
        def y(self, value):
            """y attr setter"""

            self.__y = value
