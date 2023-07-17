#!/usr/bin/python3
"""
Rectangle class that inherits from Base
"""
from models.base import Base


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

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
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
        """Sets the height of the rectangle.

        Args:
            value: The new value for the height.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
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
        """Sets the x-coordinate of the rectangle's position.

        Args:
            value: The new value for the x-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
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
        """Sets the y-coordinate of the rectangle's position.

        Args:
            value: The new value for the y-coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Displays the rectangle.

        The rectangle is displayed using "#" characters, with the x and y
        coordinates determining the position of the top-left corner of the
        rectangle.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        The string representation includes information about the rectangle's
        ID, position (x and y coordinates), width, and height.

        Returns:
            A string representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle.

        The attributes can be updated using positional arguments or keyword
        arguments. The order of the positional arguments is: ID, width, height,
        x, y.

        Args:
            *args: The positional arguments.
            **kwargs: The keyword arguments.
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle.

        Returns:
            A dictionary representation of the rectangle, including its
            attributes: id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
