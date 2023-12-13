#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines two functions get_stats that reads
extracts stats in a network packet and print_stats
that prints the stats in specified format
`
File size: 14525
200: 1
300: 2
`
after every ten 10 lines
"""
import sys
from collections import defaultdict


def get_stats():
    """Extracts the data from the packet"""
    total_size = 0
    status_codes = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin):
            parts = line.split(" ")
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size
            status_codes[status_code] += 1
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


def print_stats(total_size, status_codes):
    """prints the stats in correct format"""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        print("{}:{}".format(status_code, status_codes[status_code]))


get_stats()
