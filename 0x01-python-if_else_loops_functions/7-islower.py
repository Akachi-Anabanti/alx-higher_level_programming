#!/usr/bin/python3

def islower(c):
    """checks if c is lower alphabet
    Arguments: c
    Returns: True is c is lower otherwise False
    """
    if ord(c) in range(97, 123):
        return True
    return False
