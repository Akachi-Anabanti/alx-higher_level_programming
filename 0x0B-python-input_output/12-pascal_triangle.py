#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a function that returns a list of integers
representing the pascal triangle"""


def pascal_triangle(n):
    """Returns a list of integers
    representing the pascal triangle
    if n <= 0 it returns an empty list"""

    if n <= 0:
        return []

    main = []

    for i in range(n):
        node = []
        if i == 0:
            node.append(1)
            main.append(node)
        else:
            prev = main[i - 1]
            node.append(prev[0])

            for m in range(len(prev) - 1):
                val = prev[m] + prev[m + 1]
                node.append(val)
            node.append(1)
            main.append(node)

    return (main)
