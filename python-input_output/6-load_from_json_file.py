#!/usr/bin/python3

'''Module to create obj form JSON file'''

import json


def load_from_json_file(filename):
    '''Creates obj from a JSON file'''
    with open(filename, 'r') as f:
        my_obj = json.loads(f.read())
        return my_obj
