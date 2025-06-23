#!/usr/bin/python3

'''Module to appends a string at the end of a text file'''


def append_write(filename="", text=""):
    '''
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.
    Args:
        filename (str): The name of the file to append to
        text (str): The text content to append to the file
    Returns:
        int: The number of characters added to the file
    '''
    with open(filename, 'a') as f:
        return f.write(text)
