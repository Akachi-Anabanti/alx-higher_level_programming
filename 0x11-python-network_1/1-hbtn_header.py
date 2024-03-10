#!/usr/bin/python3
"""A script that takes a url,
sends a request and displays the value of
X-Request-Id"""
import urllib.request


if __name__ == "__main__":
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as req:
        res = req
    print(res.getheader("X-Request-Id"))
