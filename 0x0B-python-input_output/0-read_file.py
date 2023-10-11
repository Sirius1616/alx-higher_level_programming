#!/usr/bin/python3

def read_file(filename=""):
    """
    A function that reads a file
    """
    with open('filename', 'r', encoding='utf-8) as file:
        rd_file = file.read()
        print('{}'.format(rd_file))
