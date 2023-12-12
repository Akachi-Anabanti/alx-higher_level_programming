#!/usr/bin/python3
# Author: Anabanti Akachi

"""A Class that defines a student"""


class Student:
    """A class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the class"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """Returns a dictionary representation of
        the class for the attr"""

        if attrs and type(attrs) == list \
                and all(type(item) == str for item in attrs):
            return {name: getattr(self, name) for name in attrs
                    if hasattr(self, name)}

        return self.__dict__
