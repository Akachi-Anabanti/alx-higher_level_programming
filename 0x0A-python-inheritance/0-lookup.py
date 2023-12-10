#!/usr/bin/python3
# Author: Anabanti Akachi

"""A function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """A function that returns a list of
    available attributes and methos of obj
    """
    if isinstance(obj, object):
        return dir(obj)
