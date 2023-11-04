#!/usr/bin/python3
"""A square class"""


class Square:
    """A class of a square based on 3-square.py"""

    def __init__(self, size=0):
        """Initiallizing the square object

        Args:
            size(int): the size of the square
        Raises:
            TypeError: if the type of size is not an int
            ValueError: if the value of the size is negative
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A function that returns th area of the square"""

        return (self.__size * self.__size)


