#!/usr/bin/python3
class Square:
    """A class for squaring based on 1-square.py"""


    def __init__(self, size=0):
        """Init function to initialize the parameters
        arguments:
            size  ----  the size of the square that would be measured in meter

        return:
            there shall be no return value"""

        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        except (TypeError, ValueError) as err:
            print(err)
