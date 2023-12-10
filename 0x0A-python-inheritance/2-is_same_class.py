#!/usr/bin/python3
# Author: Anabanti Akachi

"""Supplies a function that returns true
an object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is instance of a_class"""

    if isinstance(obj, a_class):
        return (True)
    return (False)
