#!/usr/bin/python3

'''Module to return python obj rep by JSON str'''


import json


def from_json_string(my_str):
    '''
    Converts JSON str to python obj
    Args:
        my_obj: JSON str
    returns:
        python obj
    '''
    py_str = json.loads(my_str)
    return py_str
