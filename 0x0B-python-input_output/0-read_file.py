#!/usr/bin/python3
"""defines a class"""


def read_file(filename=""):
    """prints a file out"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
