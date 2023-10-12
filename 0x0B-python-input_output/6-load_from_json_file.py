#!/usr/bin/python3
"""Writting an object to a text file"""
import json


def load_from_json_file(filename):
    """a function that writes an Object to a text file, 
    using a JSON representation
    
    Args:
        my_obj(str): The normal python object
        filename(str): The file to write to
    """
    with open(filename, 'r') as file:
        rd_file = json.load(file)
