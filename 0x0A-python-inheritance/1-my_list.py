#!/usr/bin/python3
"""
create subclass of list
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """initialize the class"""
        print(sorted(self))
