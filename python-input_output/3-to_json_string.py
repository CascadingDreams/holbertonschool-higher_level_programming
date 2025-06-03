#!/usr/bin/python3

'''Module to return JSON rep of an object'''


import json


def to_json_string(my_obj):
    '''
    Returns the JSON rep of a string obj.
    Args:
        my_obj: python object to convert
    Returns:
        string in JSON
    '''
    json_obj = json.dumps(my_obj)
    return json_obj
