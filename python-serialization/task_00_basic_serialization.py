#!/usr/bin/python3

'''Basic serialization module'''


import json


def serialize_and_save_to_file(data, filename):
    '''Save Python dict to JSON file'''
    with open(filename, "w") as f:
        json.dump(data, f)
    pass


def load_and_deserialize(filename):
    ''' Load JSON file back to Python dict'''
    with open(filename, "r") as f:
        return json.load(f)
    pass
