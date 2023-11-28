#!/usr/bin/python3
# Author: Anabanti Akachi
# --*-- coding: utf-8 --*--
"""This module supplies a function say_my_name
that prints the concatenated result of first name and
last name, example
>>> say_my_name("Akachi", "Anabanti")
My name is Akachi Anabanti
"""


def say_my_name(first_name, last_name=""):
    """prints the formatted text My name is <first_name> <last_name>

    Arguments:
        first_name (str): The first name
        last_name(str, optional): The last name

    Raises:
        TypeError: If either first_name or last_name is not of the
            type str
        ValueError: If length of first_name is zero or either
            first_name or last_name is not a valid string.

    Prints the formatted first_name and last_name to stdout
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    if len(first_name) == 0:
        raise ValueError("first_name cannot be empty")

    for c in first_name:
        if ord(c) not in range(64, 91) and ord(c) not in range(97, 123):
            raise ValueError("first_name is not a valid string")

    for c in last_name:
        if ord(c) not in range(64, 91) and ord(c) not in range(97, 123) \
                and len(last_name) != 0:
            raise ValueError("last_name is not a valid string")

    print("My name is {} {}".format(first_name, last_name))
