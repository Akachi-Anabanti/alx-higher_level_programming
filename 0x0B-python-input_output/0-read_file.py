#!/usr/bin/python3
# Author: Anabanti Akachi

"""Supplies a function that reads a text file"""


def read_file(filename=""):
    """reads a text file and prints to stdout"""
    if filename is None or len(filename) < 1:
        pass
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
