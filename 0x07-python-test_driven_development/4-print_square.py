#!/usr/bin/python3
# Author: Akachi Anabanti
# --*-- coding: utf-8 --*--
"""This module supplies a function print_square
that takes an integer size as it's only argument
and prints the square using the characterm '#'
example
>>> print_square(2)
##
##
"""


def print_square(size):
    """Prints a square of size size with '#' """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
    if size == 0:
        print("")
