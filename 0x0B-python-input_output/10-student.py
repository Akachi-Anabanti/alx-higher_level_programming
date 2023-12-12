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
        if (attrs) and isinstance(attrs, list) \
                and all(isinstance(item, str) for item in attrs):

            old_dict = vars(self)
            new_dict = dict()
            for name in attrs:
                if name in old_dict.keys():

                    new_dict.update({name: old_dict[name]})

            return (new_dict)
        return (vars(self))
