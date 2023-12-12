#!/usr/bin/python3
# Author: Anabanti Akachi

"""defines a function that writes an object to a file
in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """Saves my_obj to filename in JSON"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
