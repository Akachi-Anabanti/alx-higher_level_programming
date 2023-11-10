#!/usr/bin/python3

roman_nums = 'ivxlcdm'
mapping = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


def clean_string(roman_string):
    """
    Cleans the string and only returns only
    Roman numerals
    """

    roman_string = roman_string.lower()
    clean_roman_string = ""

    for c in roman_string:
        if c not in roman_nums:
            continue
        clean_roman_string += c
    return clean_roman_string.lower()


def roman_to_int(roman_string):
    """
    Converts the roman numeral to int
    """

    if not isinstance(roman_string, str) or roman_string is None \
            or len(roman_string) == 0:
        return 0

    roman_string = clean_string(roman_string)

    result = 0
    prev_value = 0

    for numeral in reversed(roman_string):
        value = mapping[numeral]

        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
