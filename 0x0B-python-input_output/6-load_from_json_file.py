#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a function that creates an obj
supplied by a JSON file"""
import json


def load_from_json_file(filename):
    """loads object from JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
