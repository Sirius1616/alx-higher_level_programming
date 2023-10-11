#!/usr/bin/python3
"""
A function that reads a file
"""

def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout:
    """
    with open('filename', 'r', encoding='utf-8') as file:
        rd_file = file.read()
        print(rd_file, end="")
