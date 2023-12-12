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

    def to_json(self):
        """Returns a dictionary representation of
        the class"""

        return (vars(self))
