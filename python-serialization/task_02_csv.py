#!/usr/bin/python3

"""CSV to JSON conversion module"""


import csv
import json


def convert_csv_to_json(csv_filename):
    '''Convert CSV file to JSON format'''
    try:
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w") as f:
            json.dump(data, f)
        return True
    except FileNotFoundError:
        return False
