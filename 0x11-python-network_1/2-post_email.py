#!/usr/bin/python3
"""A script that sends a post request
with an email address"""
import urlib.request
import urllib.parse


if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
