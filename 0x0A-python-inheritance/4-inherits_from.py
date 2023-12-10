#!/usr/bin/python3
# Author: Anabanti Akachi
"""Supplies a function that returns True if the object
is an instance of a class that inherited (directly or
indirectly) from the specified class; otherwise false
"""


def inherits_from(obj, a_class):
    """Returns True if obj is subclass of a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
