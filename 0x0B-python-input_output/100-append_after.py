#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a function that inserts a line of text to a file
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string to filename after each line containing
    search_string"""

    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)  # resets to the begining of the file
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
