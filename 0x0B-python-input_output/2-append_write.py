#!/usr/bin/python3
# Author: Anabanti Akachi
"""Defines a function that appends to a txt file in utf-8"""


def append_write(filename="", text=""):
    """Writes to a txt file in UTF-8
    Args:
        filename (str): Name of the txt file
        text (str): The text to be appended
    Returns:
        The number of characters written
    """

    with open(filename, mode='a', encoding="utf-8") as f:
        return (f.write(text))
