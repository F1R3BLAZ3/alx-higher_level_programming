#!/usr/bin/python3
from models.base import Base
"""
Rectangle class that inherits from Base
"""


class Rectangle(Base):
    """Rectangle class for representing rectangles.

    This class inherits from the Base class and adds attributes and methods
    specific to rectangles.

    Attributes:
        width: The width of the rectangle.
        height: The height of the rectangle.
        x: The x-coordinate of the rectangle's position.
        y: The y-coordinate of the rectangle's position.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle instance.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle's position.
            y: The y-coordinate of the rectangle's position.
            id: An optional integer representing the ID of the instance.
                If not provided, a new ID is assigned based on the number
                of existing instances.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: The new value for the width.
        """
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value: The new value for the height.
        """
        self.__height = value

    @property
    def x(self):
        """The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle's position.

        Args:
            value: The new value for the x-coordinate.
        """
        self.__x = value

    @property
    def y(self):
        """The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle's position.

        Args:
            value: The new value for the y-coordinate.
        """
        self.__y = value
