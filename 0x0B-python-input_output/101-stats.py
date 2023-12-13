#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a script that reads network packet of the form
`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>`
and prints the stats in specified format

`
File size: 14525
200: 1
300: 2
`
after every ten 10 lines
"""
import sys
from collections import defaultdict


# Extracts the data from the packet
total_size = 0
status_codes = defaultdict(int)

try:
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.split(" ")
        status_code = parts[len(parts)- 2]
        file_size = int(parts[len(parts) -1])

        total_size += file_size
        status_codes[status_code] += 1
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for status_code in sorted(status_codes.keys()):
                print("{}:{}".format(status_code, status_codes[status_code]))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        print("{}:{}".format(status_code, status_codes[status_code]))
