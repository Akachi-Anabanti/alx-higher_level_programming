#!/usr/bin/python3
# Author: Anabanti Akachi
# --*-- coding: utf-8 --*--
"""This module supplies a function, add_integer
and returns the sumexample
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """returns the sum of two integers a and b.
    The arguments are first typecasted to int.
    A TypeError is raised if neither a nor b is an integer"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
