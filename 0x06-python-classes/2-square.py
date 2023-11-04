#!/usr/bin/python3
"""A class for square"""

class Square:
    """Class that defines properties of square by: (based on 1-square.py)."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size(int): size of the square (1 side).
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
