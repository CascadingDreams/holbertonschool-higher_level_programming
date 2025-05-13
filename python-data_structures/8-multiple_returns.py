#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        return (str_len, None)
    first_c = sentence[0]
    return (str_len, first_c)
