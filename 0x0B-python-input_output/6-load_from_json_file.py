#!/usr/bin/python
# Author: Anabanti Akachi

"""Defines a function that creates an object
supplied by a JSON file"""
import json


def load_from_json_file(filename):
    """loads object from JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
