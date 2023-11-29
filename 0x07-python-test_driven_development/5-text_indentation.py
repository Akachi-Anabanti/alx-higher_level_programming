#!/usr/bin/python3
# Author: Anabanti Akachi
# --*-- coding: utf-8 --*--
"""
This module supplies a function ```text_indentation```
that takes a string text and prints a text with 2 lines after
each of the character '.', '?', ':', example
>>> text_indentation("Hello! my name is Akachi.\
        How are you? I hope you are fine.")
Hello! my name is Akachi.
<BLANKLINE>
How are you?
<BLANKLINE>
I hope you are fine.
<BLANKLINE>
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
    '.', '?', ':'
    Arguments:
        text (str): The text to be tokenized
    Raises:
        TypeError: if text is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    split_chars = ['.', '?', ':']
    token = ""

    for char in text:
        token += char
        if char in split_chars:
            token = token.strip()
            print(token)
            print("")
            token = ""
    print(token.strip(), end="")
