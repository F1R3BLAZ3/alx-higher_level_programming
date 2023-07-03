#!/usr/bin/python3

"""This module defines a Rectangle class."""


class Rectangle:
    """
    This class represents a rectangle.
    """
    def __init__(self, width=0, height=0):

        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__size = value

    @property
    def height(self):

        return self.__width

    @width.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__size = value
