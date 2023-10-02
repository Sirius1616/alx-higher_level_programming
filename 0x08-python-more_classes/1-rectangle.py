#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """
    defines a rectangle by: (based on 0-rectangle.py)

    Attributes:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Creates an instance of rectangle

        Args:
            width(int, optional): the width of the rectangle
            height(int, optional): the height of the rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets the width of the rectangle

        Returns:
            int: width of th rectangle"""

        return self.width

    @property
    def height(self):
        """Retrieves the height of the rectangle

        Returns:
            int: the height of the rectangle"""

        return self.height


    @width.setter
    def width(self, value):
        """setter for width
        
        Args:
            value(int): the value of the width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value(int): the value of the height

        Raises:
            TypeError: heigth must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
