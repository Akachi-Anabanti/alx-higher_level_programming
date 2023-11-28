#!/usr/bin/python3
# Author: Akachi Anabanti
# --*-- coding:utf-8 --*---
"""This module supplies a function that
divides a matrix, example
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
[[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
"""

def matrix_divided(matrix, div):
    """Returns the result of a matrix divided by div"""

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if not all(type(item) in [int, float] for item in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(len(matrix) - 1):
        if  i + 1 <= len(matrix) - 1 and len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same size")

    return [[round(item / div, 2) for item in row] for row in matrix]
