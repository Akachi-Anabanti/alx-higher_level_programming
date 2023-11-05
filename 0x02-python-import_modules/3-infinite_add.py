#!/usr/bin/python3

# Infinite addition


# Import modules
import sys


def add():

    args = sys.argv[1:]

    total = 0

    for arg in args:
        total = total + int(arg)
    print("{}".format(total))


if __name__ == "__main__":
    add()
