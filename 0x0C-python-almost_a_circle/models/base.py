#!/usr/bin/python3
"""Defines a base model class."""
import json

class Base:
    """defines a base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string"""
        if list_dictionaries is None or list_dictionaries = []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs"""
        
