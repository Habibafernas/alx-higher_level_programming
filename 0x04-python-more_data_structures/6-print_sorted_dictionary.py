#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    k = list(a_dictionary.keys())
    k.sort()
    for key in k:
        print("{}: {}".format(key, a_dictionary[key]))
