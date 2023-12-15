#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a Base class"""
import json


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

    def to_json_string(list_dictionaries):
        """returns the json representation of
        list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '"[]"'
        return json.dumps(list_dictionaries)
