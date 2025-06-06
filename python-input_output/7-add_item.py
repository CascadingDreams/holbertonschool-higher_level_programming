#!/usr/bin/python3

"""
Script that adds command line arguments to a list and saves to JSON file.

This script loads existing data from add_item.json (or creates empty list),
adds all command line arguments to the list, and saves back to the file.

Usage: ./7-add_item.py [arg1] [arg2] [arg3] ...
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_data = []

new_args = sys.argv[1:]
existing_data.extend(new_args)
save_to_json_file(existing_data, "add_item.json")
