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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of
        list_dictionaries
        Args:
            list_dictionaries (list): list of dict
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method, writes the JSON string
        representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
