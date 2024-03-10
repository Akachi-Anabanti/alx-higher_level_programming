#!/usr/bin/python3
"""A script that displays header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    re = request.post(url, data={"email": email})

    print(re.text)
