#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a function that returns the dictionary description
with simple data structure for JSON serilization of an object"""


def class_to_json(obj):
    """returns the dictionary description with
    simple datat structure (list, dictionary, string, integer,
    boolean) for JSON serialization of an object"""

    return(vars(obj))
