#!/usr/bin/python3
"""A class of list"""


class MyList(list):
    """A class that inherits from list"""
    def __init__(self):
        super().__init__()


    def print_sorted(self):
        """A funtion that prints a sorted list"""
        print(sorted(self))

