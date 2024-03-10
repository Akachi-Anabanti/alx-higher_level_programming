#!/usr/bin/python3
"""A script that uses 'requests'
module to send get requests"""
import requests


if __name__ == "__main__":
    re = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(re.text)))
    print("\t- content: {}".format(re.text))
