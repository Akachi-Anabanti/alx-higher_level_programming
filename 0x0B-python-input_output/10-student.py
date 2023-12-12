#!/usr/bin/python3
# Author: Anabanti Akachi

"""A Class that defines a student"""


class Student:
    """A class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of
        the class for the attr"""
        if attrs is None:
            return vars(self)

        if attrs and isinstance(attrs, list) \
                and all(isinstance(item, str) for item in attrs):
            return {name: getattr(self, name) for name in attrs
                    if hasattr(self, name)}

        return vars(self)
