#!/usr/bin/python3

'''Module to write obj to txt file in JSON'''

import json


def save_to_json_file(my_obj, filename):
    '''Converts obj to JSON then writes to file'''
    with open(filename, 'w') as f:
        json_obj = json.dumps(my_obj)
        f.write(json_obj)
