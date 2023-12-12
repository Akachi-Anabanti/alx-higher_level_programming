#!/usr/bin/python3
# Author: Anabanti Akachi
"""Defines a function that writes to a txt file in utf-8"""


def write_file(filename="", text=""):
    """Writes to a txt file in UTF-8
    Args:
        filename (str): Name of the txt file
        text (str): The text to be written
    Returns:
        The number of characters written
    """

    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(text))
