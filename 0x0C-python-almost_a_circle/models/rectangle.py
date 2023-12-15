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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x attr getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x attr setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y attrr getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y attr setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display the triangle with '#'"""

        for x in range(self.__height):
            [print('#', end="") for i in range(self.__width)]
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height)
