#!/usr/bin/python3
"""A function that appends a string"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8) 
    and returns the number of characters added

    Arguments:
        filename(str): the file we need to append to
        text(str): the text to be written into the file

    Returns: The number of text appended
    """
    with open(filename, 'a', encoding='utf-8') as file:
        ap_file = file.write(text)
        return ap_file
