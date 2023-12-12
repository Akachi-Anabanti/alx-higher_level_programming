#!/usr/bin/python3
# Author: Anabanti Akachi

"""A Class that defines a student"""


class Student:
    """A class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the class
        Args:
            first_name (str): The firstname
            last_name (str): The last name
            age (int): The age
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Returns a dictionary representation of
        the class for the attr
        Args:
            attrs (list, optional): A list of str of
            required attrs
        """

        if type(attrs) == list \
                and all(type(item) == str for item in attrs):
            return {name: getattr(self, name) for name in attrs
                    if hasattr(self, name)}

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all the attributes of the student instance

        Args:
            json (dict): The new class attibutes
        """
        self.__dict__.update(json)
