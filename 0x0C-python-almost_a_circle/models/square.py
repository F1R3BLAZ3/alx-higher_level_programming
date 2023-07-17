#!/usr/bin/python3
"""Square class for representing squares.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class for representing squares.

    This class inherits from the Rectangle class andadds attributes and
    methods specific to squares.

    Attributes:
        size: The size of the square.
        x: The x-coordinate of the square's position.
        y: The y-coordinate of the square's position.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square instance.

        Args:
            size: The size of the square.
            x: The x-coordinate of the square's position.
            y: The y-coordinate of the square's position.
            id: An optional integer representing the ID of the instance.
                If not provided, a new ID is assigned based on the number
                of existing instances.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value: The new size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            A string in the format "[Square] (id) x/y - size".
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates the square with new attributes.

        The attributes can be provided either as positional arguments
        or keyword arguments.

        Args:
            *args: Positional arguments representing the attributes
                to be updated.
            **kwargs: Keyword arguments representing the attributes
                to be updated.
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise AttributeError("'{}' object has no attribute '{}'"
                                         .format(self.__class__.__name__, key))

    def to_dictionary(self):
        """Converts the square to a dictionary representation.

        Returns:
            A dictionary representing the square instance.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
