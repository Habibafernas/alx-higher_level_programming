#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    b = {}

    for key, value in a_dictionary.items():
        b.update({key: (value * 2)})
    return b
