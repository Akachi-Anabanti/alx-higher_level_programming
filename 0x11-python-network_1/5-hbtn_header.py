#!/usr/bin/python3
"""A script that displays header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    re = requests.get(url)

    print(re.headers.get("X-Request-Id"))
