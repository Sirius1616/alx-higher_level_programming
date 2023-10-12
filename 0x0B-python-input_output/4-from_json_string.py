#!/usr/bin/python3
"""A function that deserialize a json object"""


import json
def from_json_string(my_str):
    """ returns an object (Python data structure) 
    represented by a JSON string

    Args:
        my_str(str): the json object

    Returns:
        an object represented by a json string"""

    return (json.loads(my_str))
