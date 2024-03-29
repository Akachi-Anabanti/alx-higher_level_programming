#!/usr/bin/python3
"""a script that takses a letter and
sends a post request with the letter
as parameter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    re = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    try:
        data = re.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
