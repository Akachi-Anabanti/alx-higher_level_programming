#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a Base class"""


class Base:
    """Defines the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        ARGS:
            id (int): The value of id
        """

        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
