#!/usr/bin/python3
# Author: Anabanti Akachi

"""A class that inherits the list class
and prints the sorted list"""


class MyList(list):
    """Inherits the list class and
    prints a sorted list in ascending order
    """

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
