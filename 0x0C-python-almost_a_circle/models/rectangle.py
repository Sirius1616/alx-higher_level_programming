#!/usr/bin/python3

"""Module containing the Base class"""
from models.base import Base

"""Class rectangle that inherits from Base class"""

class Rectangle(Base):
    """Class rectangle that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new rectangle

        Args:
            width(int): width of new rectangle
            height(int): height of new rectangle
            x(int): x coordinate of new rectangle
            y(int): y coordinate of new rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get/set value for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value


    @property
    def height(self):
        """get/set value for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value


    @property
    def x(self):
        """get/set value for the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value


    @property
    def y(self):
        """get/set value for the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
    
        
