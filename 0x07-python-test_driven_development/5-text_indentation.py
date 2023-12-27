#!/usr/bin/python3
""" function that prints a text with 2 new lines after characters"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c == 0
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            print("\n")
        c += 1
