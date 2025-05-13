#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    first_c = sentence[0]
    if str_len == 0:
        return None
    return (str_len, first_c)
