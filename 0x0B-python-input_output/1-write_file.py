#!/usr/bin/python3
"""A function that writes to a file"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)

    Args:
        filename(str): the file to be written into
        text(str): the text to be written

    Returns: the number of characters added"""

    with open(filename, 'w', encoding='utf-8') as file:
        fw_file = file.write(text)
        return(fw_file)

