#!/usr/bin/python3
"""A class for square"""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        a function that checks the area of a square

        Args:
            none

        Return:
            the size of the square
        """
        return (self.__size**2)
