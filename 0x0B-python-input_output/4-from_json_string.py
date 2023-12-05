#!/usr/bin/python3
# 6-from_json_string.py
"""defines a class"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
