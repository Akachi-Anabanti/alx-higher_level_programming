#!/usr/bin/python3
# Author: Anabanti Akachi
"""Supplies a function that returns true if
an object is instance of, or if the object is an
instance of a class that is inherited from, the
specified class otherwise false"""


def is_kind_of_class(obj, a_class):
    "Returns True if obj is instance of a_class"
    if isinstance(obj, a_class):
        return (True)
    return (False)
