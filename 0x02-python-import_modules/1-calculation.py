#!/usr/bin/python3

# import modules
from calculator_1 import add, sub, mul, div


def calculate():
    """Perform calculations"""
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    calculate()
