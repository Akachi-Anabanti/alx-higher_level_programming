#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a func that converts a JSON string to a python object"""
import json


def from_json_string(my_str):
    """Returns a python object from JSON string my_str"""

    return (json.loads(my_str))
