#!/usr/bin/python3
"""Writting an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, 
    using a JSON representation
    
    Args:
        my_obj(str): The normal python object
        filename(str): The file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
