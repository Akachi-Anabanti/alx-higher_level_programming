#!/usr/bin/python3
# Author: Anabanti Akachi

"""A script that adds all cmdline args to a python list
and saves them to a file"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
new_items = sys.argv[1:]


if os.path.isfile(filename):
    old_items = load_from_json_file(filename)
    old_items.extend(new_items)
else:
    old_items = new_items
save_to_json_file(old_items, filename)
