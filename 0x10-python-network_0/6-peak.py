#!/usr/bin/python3

"""Defines a function that finds the
peak of a list of integers
"""


def find_peak(list_of_integers):
    """A function that finds the peak
    of a list of integers
    """
    if type(list_of_integers) != list or\
       len(list_of_integers) == 0:
        return None
    return max(list_of_integers)
