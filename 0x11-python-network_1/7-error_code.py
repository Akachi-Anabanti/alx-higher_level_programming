#!/usr/bin/python3
"""A script that displays header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    re = requests.get(url)

    if re.status_code < 400:
        print(re.text)
    else:
        print("Error code: {}".format(e.code))
