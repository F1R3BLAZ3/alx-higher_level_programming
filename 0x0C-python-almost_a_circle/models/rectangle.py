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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
