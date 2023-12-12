#!/usr/bin/python3
# Author: Anabanti Akachi

"""Supplies a function that adds a new attribute to
an object if possible"""


def add_attribute(obj, name="", value=""):
    """Adds a new attribute to an obj"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
