#!/usr/bin/python3
"""defines a class"""


def inherits_from(obj, a_class):
    """chaecks the type of an obj"""
    if issubclass(type(obj) ,a_class) and type(obj) != a_class:
        return True
    else:
        return False
